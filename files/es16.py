# Leggi un file testo.txt e conta tutte le parole contenute, anche se ripetute. Ogni riga può avere una o più parole.

file = open("testo.txt", "r", encoding="utf-8")
conta = 0
for riga in file:
    parole = riga.strip().split()
    for parola in parole:
        conta += 1
file.close()
print("Numero totale di parole:", conta)