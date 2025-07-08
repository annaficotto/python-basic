# Controllare se i valori di ogni riga, sommati, danno tutti la stessa somma

def righeConSommaUguale(m):
    # Calcolo la somma della prima riga
    somma_riferimento = 0
    for num in m[0]:
        somma_riferimento += num

    # Controllo le altre righe
    for i in range(1, len(m)):
        somma_riga = 0
        for num in m[i]:
            somma_riga += num

        if somma_riga != somma_riferimento:
            return False  # Appena ne trovo una diversa, ritorno False

    return True  # Tutte le somme sono uguali

# Esempio di utilizzo
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(righeConSommaUguale(matrice))  # Output: False
matrice2 = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 4, -1]
]
print(righeConSommaUguale(matrice2))  # Output: True