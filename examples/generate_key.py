from eosio_signer import EOSIOKey
import hashlib

# create key

# This is for instructional purposes. 
# This is not an endorsement to use this library to generate keys.
k = EOSIOKey()

print(f"private key: {k.to_wif()}")
print(f"public key:  {k.to_public()}")