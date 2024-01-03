from datetime import datetime


class BundIDKontoAktivitaetenNachrichtVonHeuteFalseOrTrue:

    def __init__(self, konto_activitaeten_nachircht_mit_zeitstempel):

        self.__konto_activitaeten_nachircht_mit_zeitstempel = konto_activitaeten_nachircht_mit_zeitstempel
        self.__zeitstempel_aus_der_nachricht = konto_activitaeten_nachircht_mit_zeitstempel.split(",")[0]


    def zeitstempel_ist_vom_aktuellen_tag(self):

        # Aktuelles Datum erhalten
        aktuelles_datum = datetime.now().date()

        # Datum aus der Kontoaktivitäten Nachricht in ein datetime-Objekt umwandeln, um das datum zu vergleichen
        date_obj = datetime.strptime(self.__zeitstempel_aus_der_nachricht, "%d.%m.%Y").date()

        # Datum vergleichen
        if date_obj > aktuelles_datum:
            # print("Das Datum liegt in der Zukunft.")
            konto_activitaeten_nachricht_ist_von_heute = False

        elif date_obj < aktuelles_datum:
            # print("Das Datum liegt in der Vergangenheit.")
            konto_activitaeten_nachricht_ist_von_heute = False

        else:
            # print("Das Datum ist heute.")
            konto_activitaeten_nachricht_ist_von_heute = True

        return konto_activitaeten_nachricht_ist_von_heute


if __name__ == '__main__':

    # Die Nachricht, die der Klasse übergeben wird, muss dieses Format haben.
    konto_activitaeten_nachricht_mit_zeitstempel = \
        "17.07.2023,12:54Anmeldung mit Benutzername & Passwort.Benutzername & Passwort"

    konto_activitaeten_nachricht_mit_zeitstempel = BundIDKontoAktivitaetenNachrichtVonHeuteFalseOrTrue(
        konto_activitaeten_nachircht_mit_zeitstempel=konto_activitaeten_nachricht_mit_zeitstempel,
    )

    zeitstempel_ist_vom_aktuellen_tag_tue_oder_false = konto_activitaeten_nachricht_mit_zeitstempel.zeitstempel_ist_vom_aktuellen_tag()

    print("zeitstempel_ist_vom_aktuellen_tag_tue_oder_false :",zeitstempel_ist_vom_aktuellen_tag_tue_oder_false)

