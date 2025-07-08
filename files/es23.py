# Leggi un file testo.txt e conta quante parole distinte contiene, ignorando maiuscole/minuscole.

file = open("testo.txt", "r", encoding="utf-8")
parole_distinte = []

for riga in file:
    parole = riga.strip().split()
    for parola in parole:
        parola = parola.lower()
        if parola not in parole_distinte:
            parole_distinte.append(parola)

file.close()
print("Numero di parole distinte:", len(parole_distinte))

# Nota: il metodo lower() converte la stringa in minuscolo, permettendo di ignorare le differenze tra maiuscole e minuscole.
# In alternativa, si può usare un set per tenere traccia delle parole distinte,
# che automaticamente gestisce le duplicazioni:
# parole_distinte = set()
# for riga in file:
#     parole = riga.strip().split()
#     for parola in parole:
#         parole_distinte.add(parola.lower())
# print("Numero di parole distinte:", len(parole_distinte))
# Questo approccio è più efficiente in termini di memoria e velocità, poiché i set non permettono duplicati e le operazioni di aggiunta sono più veloci.
# Tuttavia, l'esercizio richiede di implementare un controllo manuale, quindi abbiamo usato una lista.