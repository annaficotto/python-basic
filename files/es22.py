# Scrivi un programma che legge un file testo.txt e stampa la riga più lunga (in termini di numero di caratteri).

file = open("files/testo.txt", "r", encoding="utf-8")
massima_lunghezza = 0
riga_lunga = ""

for riga in file:
    lunghezza = len(riga.strip())
    if lunghezza > massima_lunghezza:
        massima_lunghezza = lunghezza
        riga_lunga = riga.strip()

file.close()
print("Riga più lunga:", riga_lunga)