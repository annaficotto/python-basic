# Dal file frasi.txt, copia nel file con\_sole.txt solo le righe che contengono la parola "sole".

origine = open("frasi.txt", "r", encoding="utf-8")
destinazione = open("con_sole.txt", "w", encoding="utf-8")

for riga in origine:
    if "sole" in riga:
        destinazione.write(riga)

origine.close()
destinazione.close()