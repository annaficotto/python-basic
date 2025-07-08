# Leggi il contenuto di origine.txt e copialo esattamente in copia.txt.

origine = open("origine.txt", "r", encoding="utf-8")
copia = open("copia.txt", "w", encoding="utf-8")

for riga in origine:
    copia.write(riga)

origine.close()
copia.close()