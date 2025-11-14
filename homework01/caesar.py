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
    if shift > 26:
        s: int = s % 26
    for l in plaintext:
        if 65 <= ord(l) <= 90:
            if ord(l) + shift > 90:
                ciphertext += chr((ord(l) + shift - 90) + 64)
            else:
                ciphertext += chr(ord(l) + shift)
        elif 97 <= ord(l) <= 122:
            if ord(l) + shift > 122:
                ciphertext += chr((ord(l) + shift - 122) + 96)
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
    if shift > 26:
        s: int = s % 26
    for l in ciphertext:
        if 65 <= ord(l) <= 90:
            if ord(l) - shift < 65:
                plaintext += chr(91 - (65 - (ord(l) - shift)))
            else:
                plaintext += chr(ord(l) - shift)
        elif 97 <= ord(l) <= 122:
            if ord(l) - shift < 97:
                plaintext += chr(123 - (97 - (ord(l) - shift)))
            else:
                plaintext += chr(ord(l) - shift)
        else:
            plaintext += l
    return plaintext
