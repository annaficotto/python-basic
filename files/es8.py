# Nel file numeri.txt ci sono numeri interi, uno per riga. Calcola e stampa la loro somma

file = open("files/numeri.txt", "r", encoding="utf-8")
somma = 0
for riga in file:
    numero = int(riga.strip())
    somma += numero
file.close()
print("Somma dei numeri:", somma)

# Nota: il metodo strip() rimuove gli spazi bianchi all'inizio e alla fine della stringa,
# quindi evita di considerare spazi vuoti o caratteri di nuova riga extra.