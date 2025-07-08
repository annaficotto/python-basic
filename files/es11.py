# Crea un file voti.csv in cui ogni riga contiene un nome e un voto separati da virgola. Scrivi almeno 5 righe.

file = open("voti.csv", "w", encoding="utf-8")
file.write("Anna,8\n")
file.write("Marco,6\n")
file.write("Sara,9\n")
file.write("Luca,7\n")
file.write("Giulia,10\n")
file.close()