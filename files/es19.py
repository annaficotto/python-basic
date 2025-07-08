# Controlla se il file dati.txt esiste. Se sì, leggilo e stampane il contenuto. Se no, stampa un messaggio d’errore.

try:
    file = open("files/dati.txt", "r", encoding="utf-8")
    contenuto = file.read()
    print("Contenuto del file:\n", contenuto)
    file.close()
except:
    print("Errore: il file 'dati.txt' non esiste.")