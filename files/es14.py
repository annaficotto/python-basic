# Dal file voti.csv, copia solo gli studenti con voto maggiore o uguale a 8 nel file promossi.csv.

voti = open("files/voti.csv", "r", encoding="utf-8")
promossi = open("files/promossi.csv", "w", encoding="utf-8")

for riga in voti:
    parti = riga.strip().split(",")
    voto = int(parti[1])
    if voto >= 8:
        promossi.write(riga)

voti.close()
promossi.close()