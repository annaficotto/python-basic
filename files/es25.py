# Nel file tabella.txt, ogni riga contiene numeri separati da spazio. Calcola la media dei valori di ogni riga e salvala in medie.txt, una per riga.

ingresso = open("tabella.txt", "r", encoding="utf-8")
uscita = open("medie.txt", "w", encoding="utf-8")

for riga in ingresso:
    numeri = riga.strip().split()
    somma = 0
    quanti = 0
    for n in numeri:
        somma += int(n)
        quanti += 1
    media = somma / quanti
    uscita.write(str(media) + "\n")

ingresso.close()
uscita.close()