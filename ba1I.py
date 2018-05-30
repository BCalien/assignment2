def SymbolToNumber(symbol): # "Legende" um den Basen eine Zahl zuzuordnen
    if symbol == "A":
        return 0
    if symbol == "C":
        return 1
    if symbol == "G":
        return 2
    if symbol == "T":
        return 3

def PatternToNumber(pat):
    zahl=SymbolToNumber(pat[-1]) #Beginne von hinten
    if (len(pat)>1): #das Pattern muss länger als eins sein
        zahl+=4*PatternToNumber(pat [0:-1]) #Umrechnung des Patterns in Dezimalwert (durch die Schleife entsteht automatisch die Funktion einer Potenz)
    return zahl

print(PatternToNumber("AGT"))
print(PatternToNumber("CTTCTCACGTACAACAAAATC")) #zweites Rosalindbeispiel