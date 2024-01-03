import logging
import os
import sys

import psutil
from helper.Non_selenium_hilfs_klassen.LeseAbsPfadVonDateienUndOrdnern import LeseAbsPfadVonDateienUndOrdnern

class TesteObExcelFuerDasSchreibenGeschlossenIst:

    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path

    def is_excel_open(self):
        try:
            # Überprüfen, ob der Pfad zur Excel-Datei existiert
            if not os.path.exists(self.excel_file_path):

                print(f"XLSX-ERROR : Die Excel-Datei '{self.excel_file_path}' existiert nicht.")
                return True

            # Überprüfen, ob der Excel-Prozess ausgeführt wird
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] == 'EXCEL.EXE':
                    try:
                        # Versuchen Sie nicht, auf die offenen Dateien des Prozesses zuzugreifen
                        # Stattdessen direkt auf den Dateipfad zugreifen
                        if os.path.abspath(self.excel_file_path) in process.cmdline():

                            print(f" XLSX-ERROR [PERMISSION DENIED] : {self.excel_file_path} "
                                  f" ist derzeit geöffnet."
                                  f" Bitte schließen sie die Datei und starten sie den Test erneut !!")
                            return True
                    except psutil.AccessDenied:
                        # Das Zugriffsrecht wurde verweigert, wenn versucht wird, auf den Prozess zuzugreifen
                        print(f"XLSX-ERROR : Zugriff auf Prozess verweigert. Die Excel-Datei '{self.excel_file_path}'\n"
                              f" ist möglicherweise geöffnet."
                              f" Überprüfen sie ob die Ergebnis-XLSX geöffnet ist , schließen sie die Datei un "
                              f" starten sie den Test erneut")
                        return True

            return False

        except Exception as e:

            return False


if __name__ == "__main__":

    current_path_obj = LeseAbsPfadVonDateienUndOrdnern()
    xlsx_pfad = current_path_obj.get_abs_path_to_bund_id_test_lab_execution_xlsx(
        test_execution_xlsx_name="Bund_id_Testfall_ausführung_v2.xlsx")

    excel_file_path = xlsx_pfad
    excel_checker = TesteObExcelFuerDasSchreibenGeschlossenIst(excel_file_path)

    if excel_checker.is_excel_open():
        sys.exit()
    else:
        pass
