import random

def generate_shifts(key, alphabet_length):
    random.seed(key)
    shifts = []
    for _ in range(alphabet_length):
        shifts.append(random.randrange(alphabet_length))
    return shifts


def encrypt_polyalphabetic(text, alphabet, key):
    alphabet = alphabet.upper()
    text = text.upper()
    for letter in text:
        if letter not in alphabet: text = text.replace(letter, "")
    shifts = generate_shifts(key, len(alphabet))
    ciphertext = ""
    for i, char in enumerate(text):
        index = alphabet.index(char)
        shifted_index = (index + shifts[i % len(shifts)]) % len(alphabet)
        ciphertext += alphabet[shifted_index]
    return ciphertext


def decrypt_polyalphabetic(ciphertext, alphabet, key):
    alphabet = alphabet.upper()
    ciphertext = ciphertext.upper()
    shifts = generate_shifts(key, len(alphabet))
    plaintext = ""
    for i, char in enumerate(ciphertext):
        index = alphabet.index(char)
        shifted_index = (index - shifts[i % len(shifts)]) % len(alphabet)
        plaintext += alphabet[shifted_index]
    return plaintext



alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
key = 27092
plaintext = "ПОБЕДА!!!"
ciphertext = encrypt_polyalphabetic(plaintext, alphabet, key)
decrypted_text = decrypt_polyalphabetic(ciphertext, alphabet, key)


print("Исходный текст:", plaintext)
print("Зашифрованный текст:", ciphertext)
print("Расшифрованный текст:", decrypted_text)