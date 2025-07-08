# Aggiungi lo studente “Matteo” con voto 7 in fondo al file voti.csv (senza, quindi, cancellare le altre righe).

file = open("files/voti.csv", "a", encoding="utf-8")
file.write("Matteo,7\n")
file.close()

# Nota: il file voti.csv deve esistere già, altrimenti il codice darà un errore.
# Se vuoi creare il file se non esiste, puoi usare il parametro 'a+' al posto di 'a':
# file = open("voti.csv", "a+", encoding="utf-8")