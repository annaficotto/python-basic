# Aggiungi il nome “Francesco” in fondo al file nomi.txt, senza cancellare i nomi già presenti.

file = open("files/nomi.txt", "a", encoding="utf-8")
file.write("Francesco\n")
file.close()