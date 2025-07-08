# Somma i valori della diagonale principale di una matrice. La diagonale principale è la linea di valori che va dall'angolo in alto a sinistra della matrice fino all'angolo in basso a destra

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
    ]

somma = 0
for i in range(len(m)):
    somma += m[i][i]
print(somma)