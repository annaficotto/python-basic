# Scrivi una lista di 5 nomi (uno per riga) nel file nomi.txt

file = open("nomi.txt", "w", encoding="utf-8")
file.write("Anna\n")
file.write("Marco\n")
file.write("Lucia\n")
file.write("Davide\n")
file.write("Sara\n")
file.close()