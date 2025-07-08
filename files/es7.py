# Nel file testo.txt è presente un testo qualsiasi. Conta quante volte compare la parola esatta "sole"

file = open("files/testo.txt", "r", encoding="utf-8")
conta = 0
for riga in file:
    parole = riga.split()
    for parola in parole:
        if parola == "sole":
            conta += 1
file.close()
print("La parola 'sole' appare:", conta, "volte")

# Nota: questo codice conta solo le occorrenze esatte della parola "sole".
# Se vuoi contare anche le varianti come "Sole" o "SOLE", puoi
# usare il metodo lower() per convertire le parole in minuscolo prima del confronto:
# if parola.lower() == "sole":
#     conta += 1
# In questo modo, il conteggio sarà case-insensitive e considererà tutte le vari
# ante della parola "sole" indipendentemente dal caso.