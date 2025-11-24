"""caesar cipher"""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    shift = shift % 26
    la = ord("a")
    ha = ord("A")
    lz = ord("z")
    hz = ord("Z")
    for l in plaintext:
        if ha <= ord(l) <= hz:
            if ord(l) + shift > hz:
                ciphertext += chr((ord(l) + shift - hz) + ha - 1)
            else:
                ciphertext += chr(ord(l) + shift)
        elif la <= ord(l) <= lz:
            if ord(l) + shift > lz:
                ciphertext += chr((ord(l) + shift - lz) + la - 1)
            else:
                ciphertext += chr(ord(l) + shift)
        else:
            ciphertext += l
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    shift = shift % 26
    la = ord("a")
    ha = ord("A")
    lz = ord("z")
    hz = ord("Z")
    for l in ciphertext:
        if ha <= ord(l) <= hz:
            if ord(l) - shift < ha:
                plaintext += chr(hz + 1 - (ha - (ord(l) - shift)))
            else:
                plaintext += chr(ord(l) - shift)
        elif la <= ord(l) <= lz:
            if ord(l) - shift < la:
                plaintext += chr(lz + 1 - (la - (ord(l) - shift)))
            else:
                plaintext += chr(ord(l) - shift)
        else:
            plaintext += l
    return plaintext
