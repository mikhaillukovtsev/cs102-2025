"""scytale cipher"""


def encrypt_scytale(plaintext, n):
    plaintext = list(plaintext)
    m = (len(plaintext) + n - 1) // n
    matrix = [[] for _ in range(m)]

    for i, char in enumerate(plaintext):
        r = i // n
        matrix[r].append(plaintext[char])

    if len(matrix[-1]) < n:
        for i in range(n - len(matrix[-1])):
            matrix[-1].append("*")

    ciphertext = ""

    for col in range(n):
        for row in range(m):
            ciphertext += matrix[row][col]

    return ciphertext
