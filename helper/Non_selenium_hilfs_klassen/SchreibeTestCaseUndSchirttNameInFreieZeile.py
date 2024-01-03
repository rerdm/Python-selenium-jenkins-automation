import openpyxl
import time



class SchreibeTestCaseUndSchirttNameInFreieZeile:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [21.09.2023]
    Diese klasse geht die ErgebnisExcel durch und schaut nach der ersten freien Zeile,
    wenn diese gefunden wurde, werden 2 Parameter jeweils in zelle a und b geschrieben.
    ####################################################################################################################
    """

    def __init__(self, workbook, sheet):

        self.__workbook = workbook
        self.__sheet = sheet

    def schreibe_test_case_und_schritt_in_neue_zeile(self, methoden_name, schritt_oder_gesamter_testfall ):

        __count_rows = 1

        for row in self.__sheet.iter_rows(values_only=True):

            if row[0] == None:
                print("Leere Zeile gefunden :",__count_rows )
                break

            __count_rows = __count_rows + 1

        print(f"Test-Fall und Schritt wurde nicht in Excel gefunden - Erstelle Testfall: {methoden_name} und :{schritt_oder_gesamter_testfall} in zeile {__count_rows}")
        self.__sheet['A'+str(__count_rows)] = methoden_name
        self.__sheet['B'+str(__count_rows)] = schritt_oder_gesamter_testfall


if __name__ == '__main__':

    # Öffne die Excel-Datei
    excel_file_path = 'Bund_id_Testfall_ausführung_new.xlsx'  # Passe 'deine_datei.xlsx' entsprechend deinem Dateinamen an
    workbook = openpyxl.load_workbook(excel_file_path)

    # Wähle das gewünschte Arbeitsblatt aus
    sheet_name = 'Ausführung - Auto Test BundID'  # Passe den Namen des Arbeitsblatts an
    sheet = workbook[sheet_name]

    methoden_name = "methoden_name"
    schritt_oder_gesamter_testfall = "schritt_oder_gesamter_testfall"

    x = SchreibeTestCaseUndSchirttNameInFreieZeile(
        workbook=workbook,
        sheet=sheet,
        file_path=excel_file_path
    )

    x.schreibe_test_case_und_schritt_in_neue_zeile(
        methoden_name=methoden_name,
        schritt_oder_gesamter_testfall=schritt_oder_gesamter_testfall
    )




