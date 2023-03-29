# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 01 October 2022

import ecdsa
import hashlib
import base58

# Generate a new private key
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Derive the corresponding public key
public_key = private_key.get_verifying_key()

# Hash the public key using SHA256
public_key_bytes = public_key.to_string()
sha256_hash = hashlib.sha256(public_key_bytes).digest()

# Hash the SHA256 hash using RIPEMD-160
ripemd160_hasher = hashlib.new('ripemd160')
ripemd160_hasher.update(sha256_hash)
ripemd160_hash = ripemd160_hasher.digest()

# Add the network byte (0x00 for mainnet) to the RIPEMD-160 hash
address_bytes = b'\x00' + ripemd160_hash

# Generate the checksum by hashing the address twice using SHA256
checksum = hashlib.sha256(hashlib.sha256(address_bytes).digest()).digest()[:4]

# Append the checksum to the address bytes
address_bytes += checksum

# Encode the address using base58 encoding
address = base58.b58encode(address_bytes)

# Print the private key, public key, and address
print("Private key: {}".format(private_key.to_string().hex()))
print("Public key: {}".format(public_key.to_string().hex()))
print("Address: {}".format(address.decode('utf-8')))
