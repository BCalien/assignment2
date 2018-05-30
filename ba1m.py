def numberToPattern(x, k):
    if k == 1:
        return numberToSymbol(x) #für den Fall dass die kmer-Länge nur eins entspricht
    return numberToPattern(x//4, k - 1) + numberToSymbol(x % 4) #Umrechnung des Wertes, die 4 steht dabei für die Anzahl der einzunehmenden Variablen (also die vier Basen)


def numberToSymbol(x): #"Legende" für Zahlenwert der Basen
    if x == 0:
        return "A"
    if x == 1:
        return "C"
    if x == 2:
        return "G"
    if x == 3:
        return "T"


print(numberToPattern(45, 4)) #Zeige die ausgeführte Funktion für gegebenen "Wert" einer gewissen kmer-Länge
print(numberToPattern(5353, 7)) #zweites Beispiel aus Rosalind