# Umbenennung der Datei zu test_addiere_zahlen.py
import pytest

def addiere_zahlen(a, b):
    return a + b

def test_positive_zahlen():
    zahl1 = 5
    zahl2 = 10
    erwartetes_ergebnis = 15

    ergebnis = addiere_zahlen(zahl1, zahl2)
    assert ergebnis == erwartetes_ergebnis, f"Fehler: {zahl1} + {zahl2} sollte {erwartetes_ergebnis} ergeben, aber es ergibt {ergebnis}"

def test_negative_zahlen():
    zahl1 = -3
    zahl2 = -7
    erwartetes_ergebnis = -10

    ergebnis = addiere_zahlen(zahl1, zahl2)
    assert ergebnis == erwartetes_ergebnis, f"Fehler: {zahl1} + {zahl2} sollte {erwartetes_ergebnis} ergeben, aber es ergibt {ergebnis}"

def test_gemischte_zahlen():
    zahl1 = 8
    zahl2 = -4
    erwartetes_ergebnis = 5

    ergebnis = addiere_zahlen(zahl1, zahl2)
    assert ergebnis == erwartetes_ergebnis, f"Fehler: {zahl1} + {zahl2} sollte {erwartetes_ergebnis} ergeben, aber es ergibt {ergebnis}"

if __name__ == "__main__":
    pytest.main()
