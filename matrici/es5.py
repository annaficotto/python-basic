# Crea la trasposta di una matrice (le righe diventano colonne e viceversa)

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
    ]

m_trasposta = []
for i in range(len(m[0])):          # ciclo sulle colonne
    nuova_riga = []
    for j in range(len(m)):         # ciclo sulle righe
        nuova_riga.append(m[j][i])
    m_trasposta.append(nuova_riga)