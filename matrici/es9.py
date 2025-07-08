# Conta il numero di valori pari nella matrice

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
    ]

conta = 0
for riga in m:
    for valore in riga:
        if valore % 2 == 0:
            conta += 1
print(conta)