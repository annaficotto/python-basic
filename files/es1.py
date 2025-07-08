# Crea un file chiamato saluto.txt e scrivi al suo interno la frase “Ciao mondo!”.

file = open("files/saluto.txt", "w", encoding="utf-8")
file.write("Ciao mondo!")
file.close()