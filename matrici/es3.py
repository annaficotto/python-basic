# Calcola la somma di tutti gli elementi della matrice.

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
    ]

somma = 0
for riga in m:
    for valore in riga:
        somma += valore
print(somma)