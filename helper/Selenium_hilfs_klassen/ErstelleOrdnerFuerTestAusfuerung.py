import logging
import os
import sys


class ErstelleOrdnerFuerTestCaseAusfuerung:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: []
    Klasse: [ErstelleOrdnerFuerTestCaseAusfuerung]
    Methoden: [erstelle_order]
    Staus [FINAL]
    Funktion:
    Diese Klasse erstellt einen Ordner, für die Test-Case Ausführung eines Test-Sets.
    ####################################################################################################################
    """

    def __int__(self):

        self.abs_pfad_zum_test_case_aufuerhungs_ordner = ""

    def erstelle_order(self, abs_pfad_zum_test_case_aufuerhungs_ordner):

        try:
            os.mkdir(abs_pfad_zum_test_case_aufuerhungs_ordner)

        except:
            sys.exit("ERROR: Test-Case Ausführungsordner konnte nicht erstellt werden")
