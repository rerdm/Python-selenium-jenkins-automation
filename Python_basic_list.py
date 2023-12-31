
def addiere_listen(liste1, liste2):
    # Überprüfen, ob beide Listen die gleiche Länge haben
    if len(liste1) != len(liste2):
        print("Die Listen müssen die gleiche Länge haben.")
        return

    # Listen elementweise addieren
    summe_liste = [a + b for a, b in zip(liste1, liste2)]

    # Ergebnis ausgeben
    print("Die Summe der Listen ist:", summe_liste)

# Beispielaufruf
liste_a = [1, 2, 3]
liste_b = [4, 5, 6]

addiere_listen(liste_a, liste_b)


