# Ruotare la matrice di 90° in senso orario

def ruota90(m):
    n = len(m)
    # Creo una matrice vuota n x n
    ruotata = []
    for i in range(n):
        ruotata.append([0] * n)

    # Ruoto la matrice: ogni elemento m[i][j] va in ruotata[j][n-1 - i]
    for i in range(n):
        for j in range(n):
            ruotata[j][n - 1 - i] = m[i][j]

    return ruotata

# Esempio di utilizzo
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m_ruotata = ruota90(m)
print(m_ruotata)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]