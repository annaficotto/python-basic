# Crea una matrice 3x4 formata solo da zeri e stampala.

numero_righe, numero_colonne = 3, 4
m = [] # lista vuota
for i in range(numero_righe):
    riga = [] # lista vuota per la riga corrente
    for j in range(numero_colonne):
        riga.append(0) # aggiungo uno zero alla riga corrente
    m.append(riga) # aggiungo la riga alla matrice


# Esempio di utilizzo
print("Matrice 3x4 formata da zeri:")
for riga in m:
    print(riga)

# oppure in modo più compatto
print(m)  # Stampa l'intera matrice in un'unica riga