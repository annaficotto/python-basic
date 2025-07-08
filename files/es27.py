# Usando il file generato con makeFile, scrivi un programma che lo legge e calcola la media del primo numero di ogni riga e del secondo numero di ogni riga.\\
# Il file contiene due numeri interi separati da spazio in ogni riga.

file = open("out.txt", "r", encoding="utf-8")

somma_primo = 0
somma_secondo = 0
righe = 0

for riga in file:
    parti = riga.strip().split()
    primo = int(parti[0])
    secondo = int(parti[1])

    somma_primo += primo
    somma_secondo += secondo
    righe += 1

file.close()

media1 = somma_primo / righe
media2 = somma_secondo / righe

print("Media del primo numero:", media1)
print("Media del secondo numero:", media2)