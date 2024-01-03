#from datetime import datetime


import datetime

class ErstelleZeitstempelAlsString:

    """
     ####################################################################################################################
     Autor: [Rene Erdmann]
     Erstellt am: []
     Klasse: [ErstelleZeitstempelAlsString]
     Methoden: [aktueller_zeitstempel]
     Staus [FINAL]
     Funktion:
     Diese Klasse ermöglicht es der aktuelle Zeitstempel, als String zurückzuliefern.
     Dieses ist notwendig, dass der Ordner der Test-Set-Ausführung einen eindeutigen namen bekommt.
     ####################################################################################################################
     """
    @staticmethod
    def aktueller_zeitstempel_jahr_monat_tag_stunde_minute_sekunde():

        jetzt = datetime.datetime.now()
        zeitstempel = jetzt.strftime("%Y_%m_%d_%H_%M_%S_")
        return zeitstempel
    @staticmethod
    def aktueller_zeitstempel_jahr_monat_tag_stunde_minute():

        jetzt = datetime.datetime.now()
        zeitstempel = jetzt.strftime("%Y_%m_%d_%H_%M_")
        return zeitstempel
    @staticmethod
    def aktueller_zeitstempel_jahr_monat_tag_stunde_minute_tz_doppelpunkt():

        jetzt = datetime.datetime.now()
        zeitstempel = jetzt.strftime("%Y:%m:%d|%H:%M")
        return zeitstempel



if __name__ == '__main__':

    # Beispielaufruf
    zeitstempel = ErstelleZeitstempelAlsString.aktueller_zeitstempel_jahr_monat_tag_stunde_minute_sekunde()
    print(zeitstempel)