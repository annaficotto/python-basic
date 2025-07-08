# Leggi il file voti.csv e stampa il nome dello studente con il voto più alto.

file = open("files/voti.csv", "r", encoding="utf-8")
massimo = -1
nome_top = ""

for riga in file:
    parti = riga.strip().split(",")
    nome = parti[0]
    voto = int(parti[1])
    if voto > massimo:
        massimo = voto
        nome_top = nome

file.close()
print("Il voto più alto è di", nome_top, "con", massimo)

# Nota: il metodo strip() rimuove gli spazi bianchi all'inizio e alla fine della stringa,
# quindi evita di considerare spazi vuoti o caratteri di nuova riga extra.