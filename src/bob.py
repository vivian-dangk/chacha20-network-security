import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

HOST = "192.168.56.10"
PORT = 5000

KEY = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)

print("=== ChaCha20 Bob Server ===")
print(f"Listening on {HOST}:{PORT}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()

print("Connection from:", addr)

# Receive 16-byte ChaCha20 nonce/counter
nonce = conn.recv(16)

# Receive ciphertext
ciphertext = conn.recv(4096)

print("Nonce     :", nonce.hex())
print("Ciphertext:", ciphertext.hex())

cipher = Cipher(
    algorithms.ChaCha20(KEY, nonce),
    mode=None
)

decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)

print("Plaintext :", plaintext.decode())

conn.close()
server.close()

print("SUCCESS: Message decrypted successfully.")
