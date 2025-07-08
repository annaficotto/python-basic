# Raddoppia ogni elemento della matrice

def raddoppia(m):
    for riga in m:
        for val in riga:
            val = val*2

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
raddoppia(m)