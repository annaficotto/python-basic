# Hai un file nomi.txt che contiene un nome per riga. Ordina alfabeticamente i nomi e scrivili in un nuovo file chiamato ordinati.txt.

# Lettura dei nomi
file = open("nomi.txt", "r", encoding="utf-8")
lista_nomi = []
for riga in file:
    lista_nomi.append(riga.strip())
file.close()

# Ordinamento manuale (bubble sort)
for i in range(len(lista_nomi)):
    for j in range(i + 1, len(lista_nomi)):
        if lista_nomi[i] > lista_nomi[j]:
            temp = lista_nomi[i]
            lista_nomi[i] = lista_nomi[j]
            lista_nomi[j] = temp

# Scrittura su nuovo file
file = open("ordinati.txt", "w", encoding="utf-8")
for nome in lista_nomi:
    file.write(nome + "\n")
file.close()

# Stampa dei nomi ordinati
print("Nomi ordinati:")
for nome in lista_nomi:
    print(nome)
# Nota: In alternativa, si potrebbe usare il metodo sort() di Python per ordinare la lista in modo più semplice:
# lista_nomi.sort()
# Tuttavia, l'esercizio richiede di implementare un algoritmo di ordinamento manuale, quindi abbiamo usato il bubble sort.
# Il bubble sort è semplice ma non molto efficiente per liste grandi. Per liste piccole come questa, va bene.