# genBitcoinAddress
Generates a Bitcoin address from a randomly generated private key.

## How this script works?

This is a Python script that generates a Bitcoin address from a randomly generated private key. The process involves several steps:

- Generates a new private key using the SECP256k1 elliptic curve.
- Derives the corresponding public key from the private key.
- Hashes the public key using SHA256 to create a 32-byte hash.
- Hashes the SHA256 hash using the RIPEMD-160 algorithm to create a 20-byte hash.
- Adds a network byte (0x00 for mainnet) to the RIPEMD-160 hash.
- Generates a checksum by hashing the address twice using SHA256 and taking the first 4 bytes.
- Appends the checksum to the address bytes.
- Encodes the address bytes using base58 encoding.
- The resulting address is a string of characters that starts with a '1' (or '3' for multi-signature addresses). This is a typical format for Bitcoin addresses on the mainnet.

Note: this script only generates a single address. To create multiple addresses, you would need to repeat the process with different private keys. Also, be aware that using randomly generated private keys is not considered secure for storing large amounts of Bitcoin. A more secure approach would involve using a hardware wallet or generating private keys using a secure random number generator.

## Preparation
- Install the following libraries:
```bash
pip3 install import ecdsa, hashlib, base58
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x genBitcoinAddress.py
```

## Usage
```bash
sudo python3 genBitcoinAddress.py
```

## Typical response
```
Private key: d34b7cf708770df266e1d8424a802614ec163e35293ebb160b8c92aa18601805
Public key: b70e7a7e53e4d64fbee1265a65139c199d9acbc134071347d73fbdc8130b5088bd4ae48b4db0c7c81d2c1f3fa986b06fac8194105f4bf9a6169321e33bf7bfa9
Address: 1A9ffeHBsaCyUqBevrttH22NdwBGVVx2Xa
```

## Sample script
```python
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
```

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
