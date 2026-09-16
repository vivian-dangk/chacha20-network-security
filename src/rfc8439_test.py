from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


key = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)

nonce = bytes.fromhex("01000000000000004a00000000000000")

plaintext = b"Hello, ChaCha20 RFC 8439!"

# Low-level cryptography ChaCha20 API:
# first 4 bytes = counter
# last 12 bytes = nonce
algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)

encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext)

print("=== ChaCha20 RFC 8439 Test ===")
print("Key       :", key.hex())
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext.hex())

algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)

decryptor = cipher.decryptor()
decrypted = decryptor.update(ciphertext)

print("Decrypted :", decrypted)

if decrypted == plaintext:
    print("PASS: Encryption and decryption are correct.")
else:
    print("FAIL: Decryption does not match plaintext.")
