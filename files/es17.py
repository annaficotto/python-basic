# Conta quante parole iniziano con la lettera "A" (maiuscola) nel file parole.txt.

file = open("files/parole.txt", "r", encoding="utf-8")
conta = 0
for riga in file:
    parole = riga.strip().split()
    for parola in parole:
        if parola.startswith("A"):
            conta += 1
file.close()
print("Parole che iniziano con 'A':", conta)

# Nota: il metodo startswith() verifica se la stringa inizia con il prefisso specificato.