def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    if len(keyword) < len(plaintext):
        keyword *= len(plaintext) // len(keyword) + 1
    i = 0
    for l in plaintext: 
        if keyword[i].isupper():
            k = ord(keyword[i]) - 65
        else:
            k = ord(keyword[i]) - 97
        if 65 <= ord(l) <= 90:
            if ord(l) + k > 90:
                ciphertext += chr((ord(l) + k - 90) + 64)
            else:
                ciphertext += chr(ord(l) + k)
        elif 97 <= ord(l) <= 122:
            if ord(l) + k > 122:
                ciphertext += chr((ord(l) + k - 122) + 96)
            else:
                ciphertext += chr(ord(l) + k)
        else:
            ciphertext += l
        i += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if len(keyword) < len(ciphertext):
        keyword *= len(ciphertext) // len(keyword) + 1
    i = 0
    for l in ciphertext: 
        if keyword[i].isupper():
            k = ord(keyword[i]) - 65
        else:
            k = ord(keyword[i]) - 97
        if 65 <= ord(l) <= 90:
            if ord(l) - k < 65:
                plaintext += chr(91 - (65 - (ord(l) - k)))
            else:
                plaintext += chr(ord(l) - k) 
        elif 97 <= ord(l) <= 122:
            if ord(l) - k < 97:
                plaintext += chr(123 - (97 - (ord(l) - k)))
            else:
                plaintext += chr(ord(l) - k)
        else:
            plaintext += l
        i += 1
    return plaintext