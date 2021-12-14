import sys

sys.path.append('../eosio_signer')

from eosio_signer import EOSIOKey
import hashlib
import pytest


class TestEOSIOKey:
    payload = "some important data"
    digest = hashlib.sha256(payload.encode('utf-8').rstrip()).hexdigest()

    legacy = ("EOS6JWAwA6goJmmAGwQEwbFne8zNxhuVTjgk1aLqVW9efHWhGfvwU",
              "5JU8RktQ72qFtJyiW3DJ54B2ZY6Ad83HdoGg78Nk8kUNMJEmCUg")

    r1 = ("PUB_R1_65vcmkCEJuxQ2rvYxBZSiUGP9FJPaqMfrLyakHduxEULWcBUxW",
          "PVT_R1_2sTZXHRWPfgWfn4gTD4bXjVsKRTSYBCekebBgJq1P9SW7ckoXk")

    k1 = ("PUB_K1_6ctHgq55Tt4u3ksvDw1jadhC5tytemHs8fHM4YfFVqMe4F8XWU",
          "PVT_K1_r9seSVdS9yTRmSXtLrpELLZ5dhbEqr12jLCRg5NJAWr5q8U9o")

    def signing(self, key_val: str):
        key = EOSIOKey(key_val)
        sig = key.sign(self.digest)
        assert key.verify(sig, self.digest)

    def test_verify_fail(self):
        fail_digest = hashlib.sha256("failure".encode('utf-8').rstrip()).hexdigest()
        key = EOSIOKey(self.r1[1])
        sig = key.sign(self.digest)
        assert key.verify(sig, fail_digest) == False

    def test_incorrect_keytype(self):
        key = EOSIOKey(self.r1[1])
        key_k1 = EOSIOKey(self.k1[1])
        sig = key.sign(self.digest)
        with pytest.raises(TypeError):
            key_k1.verify(sig, self.digest)

    def test_legacy(self):
        self.signing(self.legacy[1])

    def test_r1(self):
        self.signing(self.r1[1])

    def test_k1(self):
        self.signing(self.k1[1])

    def test_legacy_public_key(self):
        key = EOSIOKey(self.legacy[1])
        assert key.to_public() == self.legacy[0]

    def test_public_key_r1(self):
        key = EOSIOKey(self.r1[1])
        assert key.to_public() == self.r1[0]

    def test_public_key_k1(self):
        key = EOSIOKey(self.k1[1])
        assert key.to_public() == self.k1[0]