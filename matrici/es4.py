# Scrivi una funzione che ritorna True se la matrice è quadrata.

def e_quadrata(m):
    numero_righe = len(m) # nota 1
    for riga in m:
        if len(riga) != numero_righe:
            return False
    return True

m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[1,2], [3,4,5]]

print(e_quadrata(m1))  # True
print(e_quadrata(m2))  # False


# nota 1: len(m) ritorna il numero di righe della matrice m.
# Per ogni riga della matrice, controlliamo se il numero di elementi è uguale