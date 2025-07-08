# Trova il valore massimo e il valore minimo della matrice


def max_e_min_base(m):
    massimo = m[0][0]
    minimo = m[0][0]

    for riga in m:
        for elemento in riga:
            if elemento > massimo:
                massimo = elemento
            if elemento < minimo:
                minimo = elemento

    print("Max:", massimo, "Min:", minimo)

def max_e_min_avanzato(m):
    massimo = m[0][0]
    minimo = m[0][0]

    for riga in m:
        max_riga = max(riga)  # massimo nella riga corrente
        min_riga = min(riga)  # minimo nella riga corrente

        if max_riga > massimo:
            massimo = max_riga

        if min_riga < minimo:
            minimo = min_riga

    print("Max:", massimo, "Min:", minimo)

m = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
max_e_min_base(m)
max_e_min_avanzato(m)