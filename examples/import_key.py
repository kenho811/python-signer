from eosio_signer import EOSIOKey
import hashlib

digest = hashlib.sha256("digest".encode()).hexdigest()

# import key
# DO NOT USE these keys as they are known keys that are publicly available 
r1_key = EOSIOKey('PVT_R1_2sTZXHRWPfgWfn4gTD4bXjVsKRTSYBCekebBgJq1P9SW7ckoXk')
k1_key = EOSIOKey('PVT_K1_r9seSVdS9yTRmSXtLrpELLZ5dhbEqr12jLCRg5NJAWr5q8U9o')

# r1 signing
r1_sig = r1_key.sign(digest)

# k1 signing
k1_sig = k1_key.sign(digest)

print(f'r1_sig: {r1_sig}')
print(f'k1_sig: {k1_sig}')