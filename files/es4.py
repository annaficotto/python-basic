# Leggi tutti i nomi da nomi.txt e stampali in maiuscolo, uno per riga.

file = open("nomi.txt", "r", encoding="utf-8")
for riga in file:
    print(riga.strip().upper())
file.close()

# Nota: il metodo strip() rimuove gli spazi bianchi all'inizio e alla fine della stringa,
# quindi evita di stampare spazi vuoti o caratteri di nuova riga extra.