# Nel file numeri.txt c’è un numero per riga. Trova quale numero compare più volte e quante volte.

file = open("numeri.txt", "r", encoding="utf-8")
numeri = []
frequenze = []

for riga in file:
    numero = int(riga.strip())
    trovato = False
    for i in range(len(numeri)):
        if numeri[i] == numero:
            frequenze[i] += 1
            trovato = True
            break
    if not trovato:
        numeri.append(numero)
        frequenze.append(1)

file.close()

# Trova la frequenza massima
massimo = 0
indice = 0
for i in range(len(frequenze)):
    if frequenze[i] > massimo:
        massimo = frequenze[i]
        indice = i

print("Numero più frequente:", numeri[indice])
print("Frequenza:", massimo)

# Nota: il file numeri.txt deve esistere già, altrimenti il codice darà un errore.
# Se vuoi creare il file se non esiste, puoi usare il parametro 'a+' al posto di 'r':
# file = open("numeri.txt", "a+", encoding="utf-8")