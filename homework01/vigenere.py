"""vigenere cipher"""


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
    la = ord("a")
    ha = ord("A")
    lz = ord("z")
    hz = ord("Z")
    for l in plaintext:
        if keyword[i].isupper():
            k = ord(keyword[i]) - ha
        else:
            k = ord(keyword[i]) - la
        if ha <= ord(l) <= hz:
            if ord(l) + k > hz:
                ciphertext += chr((ord(l) + k - hz) + ha - 1)
            else:
                ciphertext += chr(ord(l) + k)
        elif la <= ord(l) <= lz:
            if ord(l) + k > lz:
                ciphertext += chr((ord(l) + k - lz) + la - 1)
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
    la = ord("a")
    ha = ord("A")
    lz = ord("z")
    hz = ord("Z")
    for l in ciphertext:
        if keyword[i].isupper():
            k = ord(keyword[i]) - ha
        else:
            k = ord(keyword[i]) - la
        if ha <= ord(l) <= hz:
            if ord(l) - k < ha:
                plaintext += chr((hz + 1) - (ha - (ord(l) - k)))
            else:
                plaintext += chr(ord(l) - k)
        elif la <= ord(l) <= lz:
            if ord(l) - k < hz:
                plaintext += chr((lz + 1) - (la - (ord(l) - k)))
            else:
                plaintext += chr(ord(l) - k)
        else:
            plaintext += l
        i += 1
    return plaintext
