import re

class ErstelleValidenTestCaseNameAusXlsxTitel:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: []
    Klasse: [ErstelleValidenTestCaseNameAusXlsxTitel]
    Methoden: [remove_spaces]
    Staus [FINAL]
    Funktion:
    Diese Klasse kann genutzt werden, um den Test-Case namen der XLsx files in einen Validen namen zu mappen.
    Ein name der als test_NAME verwenden werden kann ( da spaces .-,+ nicht erlaubt sind)
    ####################################################################################################################
    """

    def __init__(self, input_string):
        self.input_string = input_string.lower()

    def remove_spaces(self):
        #new_test_case_name = self.input_string.replace("i","hhhhh")
        new_test_case_name = self.input_string.replace("-", "_").replace(" ","_").replace("ä","ae").replace("ü","eu").replace("i","I").replace("__","")

        return new_test_case_name


if __name__ == '__main__':

    # Beispielnutzung
    input_string = "002 - Angemeldet mit Benutzername und Passwort - automatischer Logout wegen Inaktivität"
    remover = ErstelleValidenTestCaseNameAusXlsxTitel(input_string)
    string_without_spaces = remover.remove_spaces()
    print("String ohne Leerzeichen:", string_without_spaces)