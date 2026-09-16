from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


# 256-bit key = 32 bytes
key = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)

# 128-bit nonce required by cryptography's low-level ChaCha20 API
nonce = bytes.fromhex("00000000000000090000004a00000000")

plaintext = b"Hello, ChaCha20!"


# Encrypt
algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)

encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext)

print("Plaintext :", plaintext)
print("Key       :", key.hex())
print("Nonce     :", nonce.hex())
print("Ciphertext:", ciphertext.hex())


# Decrypt
algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)

decryptor = cipher.decryptor()
decrypted = decryptor.update(ciphertext)

print("Decrypted :", decrypted)


# Check result
if decrypted == plaintext:
    print("SUCCESS: Decryption matches plaintext.")
else:
    print("ERROR: Decryption does not match plaintext.")
