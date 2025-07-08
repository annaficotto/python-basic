# Somma i valori della diagonale secondaria di una matrice. La diagonale secondaria è la linea di valori che va dall'angolo in alto a destra della matrice fino all'angolo in basso a sinistra.

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
    ]

n = len(m)
somma = 0
for i in range(n):
    somma += m[i][n - 1 - i]
print(somma)