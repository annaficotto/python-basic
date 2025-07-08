# La funzione medaglie(f) fa quanto segue:
# - Legge un file CSV il cui nome è passato nel parametro 'f'
# - Usa la virgola come separatore per i campi
# - Salva i nomi delle nazioni in una lista chiamata 'nazioni'
# - Salva le medaglie (oro, argento, bronzo) in una matrice chiamata 'counts'
#   dove ogni riga rappresenta una nazione e ogni colonna un tipo di medaglia
# - Calcola:
#   - Il totale di medaglie d'oro, d'argento e di bronzo sommando le rispettive colonne
#   - Il totale di medaglie per ogni nazione (somma delle righe)
# - Scrive i totali per nazione (somma delle medaglie di ogni nazione) nel file 'totali.txt',
#   uno per riga, nello stesso ordine del file CSV originale
# - Ritorna una lista con i tre totali globali: [oro_tot, argento_tot, bronzo_tot]

def medaglie(f):
    file = open(f, "r", encoding="utf-8")
    nazioni = []
    counts = []

    prima = True
    for riga in file:
        if prima:
            prima = False  # Saltiamo intestazione
            continue
        parti = riga.strip().split(",")
        nazioni.append(parti[0])
        oro = int(parti[1])
        argento = int(parti[2])
        bronzo = int(parti[3])
        counts.append([oro, argento, bronzo])

    file.close()

    # Calcolo totali per tipo di medaglia
    totale_oro = 0
    totale_argento = 0
    totale_bronzo = 0
    for riga in counts:
        totale_oro += riga[0]
        totale_argento += riga[1]
        totale_bronzo += riga[2]

    # Scrittura dei totali per nazione su file
    out = open("files/medals_totals.txt", "w", encoding="utf-8")
    for i in range(len(nazioni)):
        totale_nazione = counts[i][0] + counts[i][1] + counts[i][2]
        out.write(nazioni[i] + ": " + str(totale_nazione) + "\n")
    out.close()

    return [totale_oro, totale_argento, totale_bronzo]

# Esempio di chiamata
totali = medaglie("files/medals.csv")
print("Totale medaglie d'oro:", totali[0])
print("Totale medaglie d'argento:", totali[1])
print("Totale medaglie di bronzo:", totali[2])