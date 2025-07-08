# Apri il file nomi.txt e conta quante righe contiene. Stampa il risultato.

file = open("nomi.txt", "r", encoding="utf-8")
conta = 0
for riga in file:
    conta += 1
file.close()
print("Numero di righe:", conta)

# Nota: il metodo readlines() può essere usato per leggere tutte le righe in una lista,
# ma in questo caso abbiamo usato un ciclo for per contare le righe senza caricare tutto il file in memoria.
# In alternativa, si può usare il metodo read() e poi contare le righe con il metodo splitlines():
# file = open("nomi.txt", "r", encoding="utf-8")
# contenuto = file.read()