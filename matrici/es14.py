# Scrivi una funzione che ritorni la matrice specchiata orizzontalmente

def specchia_orizzontalmente_base(m):
    specchiata = []
    for riga in m:
        nuova_riga = []
        i = len(riga) - 1
        while i >= 0:
            nuova_riga.append(riga[i])
            i -= 1
        specchiata.append(nuova_riga)
    return specchiata

def specchia_orizzontalmente_avanzato(m):
    specchiata = []
    for riga in m:
        nuova_riga = riga.copy()
        nuova_riga.reverse()


# Esempio di utilizzo
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m_specchiata_base = specchia_orizzontalmente_base(m)
m_specchiata_avanzato = specchia_orizzontalmente_avanzato(m)
print(m_specchiata_base)  # Output: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
print(m_specchiata_avanzato)  # Output: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]