from collections import Counter

# Step 1: Read ciphertext and guess key length
def hamming_distance(a, b):
    return sum(bin(x ^ y).count('1') for x, y in zip(a, b))

def guess_key_length(cipher_bytes, max_length=40):
    best_length = 1
    best_score = float('inf')
    for l in range(1, max_length + 1):
        blocks = [cipher_bytes[i*l:(i+1)*l] for i in range(len(cipher_bytes)//l)][:4]
        if len(blocks) < 2:
            continue
        score = sum(hamming_distance(blocks[i], blocks[i+1])/l for i in range(len(blocks)-1))
        score /= len(blocks)-1
        if score < best_score:
            best_score = score
            best_length = l
    return best_length

# Read ciphertext from file
with open('Cipher_text_11.txt', 'r') as f:
    hex_cipher = f.read().strip()

cipher_bytes = bytes.fromhex(hex_cipher)
key_length = guess_key_length(cipher_bytes)
print(f"[+] Guessed key length: {key_length}")

# Step 2: Recover the key using frequency analysis
freq = {' ': 15, 'e': 12.7, 't': 9.0, 'a': 8.1, 'o': 7.5, 'i': 6.9, 'n': 6.7}

def score_text(text):
    return sum(freq.get(chr(c).lower(), 0) for c in text)

def recover_key(cipher_bytes, key_length):
    key = bytearray()
    for i in range(key_length):
        block = cipher_bytes[i::key_length]
        best_score = -1
        best_byte = 0
        for candidate in range(256):
            decrypted = bytes([c ^ candidate for c in block])
            current_score = score_text(decrypted)
            if current_score > best_score:
                best_score = current_score
                best_byte = candidate
        key.append(best_byte)
    return bytes(key)

key = recover_key(cipher_bytes, key_length)

# Convert hex key to ASCII for readability (if possible)
hex_key = key.hex()
ascii_key = key.decode('latin-1')  # Use 'latin-1' to avoid Unicode errors

print(f"[+] Recovered key (hex): {hex_key}")
print(f"[+] Recovered key (ASCII): {ascii_key}")

# Step 3: Decrypt and save to file
def decrypt(cipher_bytes, key):
    key_repeated = (key * (len(cipher_bytes) // len(key) + 1))[:len(cipher_bytes)]
    return bytes([c ^ k for c, k in zip(cipher_bytes, key_repeated)])

decrypted = decrypt(cipher_bytes, key)

# Save decrypted text to decrypted.txt
with open('decrypted.txt', 'w', encoding='utf-8') as f:
    decrypted_text = decrypted.decode('utf-8', errors='ignore')
    f.write(decrypted_text)

# Extract and print the random string
random_string = decrypted_text[-25:]
print(f"\n[+] Random string: {random_string}")
print("[+] Decrypted text saved to decrypted.txt")