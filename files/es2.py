# Leggi e stampa il contenuto del file saluto.txt

file = open("saluto.txt", "r", encoding="utf-8")
contenuto = file.read()
print(contenuto)
file.close()