# # La funzione makeFile(nome, n, a, b, c) fa quanto segue:
# - Imposta il seed del generatore di numeri casuali a 0 per rendere i risultati ripetibili
# - Crea un file con nome indicato dal parametro 'nome'
# - Scrive esattamente 'n' righe nel file
# - Ogni riga contiene due numeri interi casuali:
#   - Il primo è compreso tra 'a' e 'b' (estremi inclusi)
#   - Il secondo è compreso tra 'b' e 'c' (estremi inclusi)
# - I due numeri sulla stessa riga sono separati da almeno uno spazio

import random

def makeFile(nome, n, a, b, c):
    random.seed(0)
    file = open(nome, "w", encoding="utf-8")

    for i in range(n):
        primo = random.randint(a, b)
        secondo = random.randint(b, c)
        file.write(str(primo) + " " + str(secondo) + "\n")

    file.close()

# Esempio di chiamata
makeFile("files/out.txt", 5, 1, 10, 20)