from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

KEY = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)

# CỐ TÌNH dùng cùng một nonce cho hai plaintext
NONCE = bytes.fromhex(
    "01000000"
    "246a4f2f4bdbea3fc9ebfcaf"
)

plaintext1 = b"Attack at dawn! Send backup."
plaintext2 = b"Attack at dusk! Send backup."

def encrypt(plaintext):
    cipher = Cipher(
        algorithms.ChaCha20(KEY, NONCE),
        mode=None
    )
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext)

ciphertext1 = encrypt(plaintext1)
ciphertext2 = encrypt(plaintext2)

# XOR hai ciphertext
xor_ciphertexts = bytes(
    a ^ b for a, b in zip(ciphertext1, ciphertext2)
)

# XOR ciphertext1 với plaintext1
# Do cùng key + nonce nên ta thu được plaintext2
recovered_plaintext2 = bytes(
    a ^ b ^ c
    for a, b, c in zip(ciphertext1, ciphertext2, plaintext1)
)

print("=== ChaCha20 Nonce Reuse Demonstration ===")

print("\nPlaintext 1 : ", plaintext1)
print("Ciphertext 1:", ciphertext1.hex())

print("\nPlaintext 2 : ", plaintext2)
print("Ciphertext 2:", ciphertext2.hex())

print("\nSame key   :", KEY.hex())
print("Same nonce :", NONCE.hex())

print("\nC1 XOR C2  :", xor_ciphertexts.hex())
print("P1 XOR P2  :", bytes(
    a ^ b for a, b in zip(plaintext1, plaintext2)
).hex())

print("\nRecovered plaintext 2:")
print(recovered_plaintext2)

if recovered_plaintext2 == plaintext2:
    print("\nDEMONSTRATION SUCCESS")
    print("Nonce reuse exposes the relationship between the two plaintexts.")
