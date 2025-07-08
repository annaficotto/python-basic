# Somma i valori che si trovano nelle due diagonali di una matrice quadrata (principale e secondaria)

def sommaDiagonali(m):
    n = len(m)
    somma_principale = 0
    somma_secondaria = 0
    for i in range(n):
        somma_principale += m[i][i]
    for i in range(n):
        somma_secondaria += m[i][n - 1 - i]
    return somma_principale + somma_secondaria

# Esempio di utilizzo
m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
    ]

somma = sommaDiagonali(m)
print(somma)  # Output: 30 (1 + 5 + 9 + 3 + 5 + 7)