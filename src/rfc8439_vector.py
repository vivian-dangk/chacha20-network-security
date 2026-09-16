from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

key = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)

nonce = bytes.fromhex( 
    "01000000" 
    "000000000000004a00000000" 
)

plaintext = (
    b"Ladies and Gentlemen of the class of '99: "
    b"If I could offer you only one tip for the future, "
    b"sunscreen would be it."
)

expected = bytes.fromhex(
    "6e2e359a2568f98041ba0728dd0d6981"
    "e97e7aec1d4360c20a27afccfd9fae0b"
    "f91b65c5524733ab8f593dabcd62b357"
    "1639d624e65152ab8f530c359f0861d8"
    "07ca0dbf500d6a6156a38e088a22b65e"
    "52bc514d16ccf806818ce91ab7793736"
    "5af90bbf74a35be6b40b8eedf2785e42"
    "874d"
)

cipher = Cipher(
    algorithms.ChaCha20(key, nonce),
    mode=None
)

encryptor = cipher.encryptor()
actual = encryptor.update(plaintext)

print("=== RFC 8439 ChaCha20 Test Vector ===")
print("Key      :", key.hex())
print("Nonce    :", nonce.hex())
print("Plaintext:", plaintext)
print("Actual   :", actual.hex())
print("Expected :", expected.hex())

if actual == expected:
    print("PASS: Ciphertext matches RFC 8439.")
else:
    print("FAIL: Ciphertext does NOT match RFC 8439.")
    print("Actual length  :", len(actual))
    print("Expected length:", len(expected))
