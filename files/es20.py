# Leggi il file persone.csv dove ogni riga è: Nome,Età. Stampa solo i nomi di chi ha più di 18 anni.

file = open("files/persone.csv", "r", encoding="utf-8")

for riga in file:
    parti = riga.strip().split(",")
    nome = parti[0]
    età = int(parti[1])
    if età > 18:
        print(nome)

file.close()