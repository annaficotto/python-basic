# Verifica che in una matrice sia presente almeno un valore pari a 0

def contiene_zero_base(m):
    for riga in m:
        for val in riga:
            if val == 0:
                return True
    return False

# Nota: Questa funzione scorre ogni riga della matrice e ogni valore in quella riga.
# Se trova un valore pari a 0, ritorna True. Se non trova alcun valore pari a 0, ritorna False.
# Questo è un esempio di ricerca di un valore specifico in una matrice.

def contiene_zero_avanzato(m):
    for riga in m:
        if 0 in riga:
            return True
    return False

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
print(contiene_zero_base(m1))  # False
print(contiene_zero_base(m2))  # True

print(contiene_zero_avanzato(m1))  # False
print(contiene_zero_avanzato(m2))  # True