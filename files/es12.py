# Leggi il file voti.csv e calcola la media dei voti.

file = open("files/voti.csv", "r", encoding="utf-8")
somma = 0
conteggio = 0

for riga in file:
    parti = riga.strip().split(",")
    voto = int(parti[1])
    somma += voto
    conteggio += 1

file.close()
media = somma / conteggio
print("Media voti:", media)

# Nota: il metodo strip() rimuove gli spazi bianchi all'inizio e alla fine della stringa,
# quindi evita di considerare spazi vuoti o caratteri di nuova riga extra.
# Se il file contiene righe vuote o formattazioni errate, potrebbe essere necessario aggiungere controlli per gestire questi casi (il nostro programma, per ora, non li gestisce).