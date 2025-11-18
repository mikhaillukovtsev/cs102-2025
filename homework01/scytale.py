"""scytale cipher"""


def encrypt_scytale(plaintext, n):
    plaintext = list(plaintext)
    m = (len(plaintext) + n - 1) // n
    matrix = [[] for _ in range(m)]
    r = 0

    for i in plaintext:
        matrix[r].append(i)
        if len(matrix[r]) == n:
            r += 1

    if len(matrix[-1]) < n:
        for i in range(n - len(matrix[-1])):
            matrix[-1].append("*")

    ciphertext = ""

    for col in range(n):
        for row in range(m):
            ciphertext += matrix[row][col]

    return ciphertext
