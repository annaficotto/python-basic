# Dal file testo.txt, copia nel file con_sole.txt solo le righe che contengono la parola "sole".

origine = open("files/testo.txt", "r", encoding="utf-8")
destinazione = open("files/sole.txt", "w", encoding="utf-8")

for riga in origine:
    if "sole" in riga:
        destinazione.write(riga)

origine.close()
destinazione.close()