# Scrivi una versione della funzione chiamata medagliereSuper(f) che fa esattamente le stesse cose, ma il file di input (es. gara.txt) non usa virgole: gli elementi sono separati da spazi o più spazi.

def medagliereSuper(f):
    file = open(f, "r", encoding="utf-8")
    nazioni = []
    counts = []

    prima = True
    for riga in file:
        if prima:
            prima = False
            continue
        parole = riga.strip().split()
        # La nazione può avere più parole: tutto tranne le ultime 3
        nome_nazione = " ".join(parole[:-3])
        oro = int(parole[-3])
        argento = int(parole[-2])
        bronzo = int(parole[-1])
        nazioni.append(nome_nazione)
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
    out = open("totali.txt", "w", encoding="utf-8")
    for i in range(len(nazioni)):
        totale_nazione = counts[i][0] + counts[i][1] + counts[i][2]
        out.write(nazioni[i] + ": " + str(totale_nazione) + "\n")
    out.close()

    return [totale_oro, totale_argento, totale_bronzo]

# Esempio di chiamata
totali = medagliereSuper("medaglie_super.txt")
print("Totale medaglie d'oro:", totali[0])
print("Totale medaglie d'argento:", totali[1])
print("Totale medaglie di bronzo:", totali[2])