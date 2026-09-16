import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

KEY_CHACHA = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)
NONCE_CHACHA = bytes.fromhex(
    "01000000246a4f2f4bdbea3fc9ebfcaf"
)

KEY_AES = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)
NONCE_AES = bytes.fromhex("00" * 16)  # AES-CTR can dung 16 byte nonce/counter

sizes = [
    ("1 KB", 1024),
    ("10 KB", 10 * 1024),
    ("100 KB", 100 * 1024),
    ("1 MB", 1024 * 1024),
    ("10 MB", 10 * 1024 * 1024),
]

def benchmark_chacha20(plaintext):
    cipher = Cipher(algorithms.ChaCha20(KEY_CHACHA, NONCE_CHACHA), mode=None)
    encryptor = cipher.encryptor()
    encryptor.update(plaintext)  # warm-up

    cipher = Cipher(algorithms.ChaCha20(KEY_CHACHA, NONCE_CHACHA), mode=None)
    encryptor = cipher.encryptor()
    start = time.perf_counter()
    encryptor.update(plaintext)
    end = time.perf_counter()
    return end - start

def benchmark_aes_ctr(plaintext):
    cipher = Cipher(algorithms.AES(KEY_AES), modes.CTR(NONCE_AES))
    encryptor = cipher.encryptor()
    encryptor.update(plaintext)  # warm-up

    cipher = Cipher(algorithms.AES(KEY_AES), modes.CTR(NONCE_AES))
    encryptor = cipher.encryptor()
    start = time.perf_counter()
    encryptor.update(plaintext)
    end = time.perf_counter()
    return end - start

print("=== ChaCha20 vs AES-256-CTR Performance Benchmark ===")
print()
header = f"{'Data size':<12}{'ChaCha20 (MB/s)':<20}{'AES-256-CTR (MB/s)':<20}"
print(header)
print("-" * len(header))

for name, size in sizes:
    plaintext = b"A" * size

    t_chacha = benchmark_chacha20(plaintext)
    t_aes = benchmark_aes_ctr(plaintext)

    tp_chacha = (size / (1024 * 1024)) / t_chacha
    tp_aes = (size / (1024 * 1024)) / t_aes

    print(f"{name:<12}{tp_chacha:<20.2f}{tp_aes:<20.2f}")

print()
print("Benchmark completed successfully.")
