from helper.Selenium_hilfs_klassen.InitialisierenDesWebdrivers import InitialisierenDesWebdrivers


class MethodenEinerKlasseAusfuehren:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [15.06.2023]
    Klasse: [BuchstabenGenerator]
    Methoden: [execute_method]
    Funktion:
    Diese Klasse kann genutzt werden um Methoden einer Klasse zu Testen.
    Dies kann hilfreich wenn die sein wenn die Pages entwickelt wurden und die einzelnen Methoden getestet werden sollen
    ####################################################################################################################
    """

    def __init__(self, klassenname, *args, **kwargs):
        self.klassenname = klassenname
        self.args = args
        self.kwargs = kwargs

    def execute_method(self, methodenname, *args, **kwargs):
        try:
            klasse = globals()[self.klassenname]
            instanz = klasse(*self.args, **self.kwargs)
            methode = getattr(instanz, methodenname)
            methode(*args, **kwargs)
        except KeyError:
            raise ValueError(f"Die Klasse '{self.klassenname}' wurde nicht gefunden.")
        except AttributeError:
            raise ValueError(f"Die Methode '{methodenname}' wurde in der Klasse '{self.klassenname}' nicht gefunden.")

        print(klasse)

# Beispielklasse

if __name__ == '__main__':

    # Initialisieren des drivers vor jedem Test ####################################################################
    driver_initialisieren = InitialisierenDesWebdrivers()
    driver = driver_initialisieren.get_chrome_driver_v14()

    driver.get("https://test.id.bund.de/de")

    ausfuehrer = MethodenEinerKlasseAusfuehren("BundID_startseite", driver, "test1", "test2")
    # Aufruf der Methode mit Werten
    ausfuehrer.execute_method("anmelde_button_klick", 5, "Test3", "Test4")
