from helper.Non_selenium_hilfs_klassen.LeseAbsPfadVonDateienUndOrdnern import LeseAbsPfadVonDateienUndOrdnern
from helper.Non_selenium_hilfs_klassen.ReporteTestCaseUndStepErgebnisseInXlsx import ReporteTestCaseUndStepErgebnisseInXlsx


from helper.Non_selenium_hilfs_klassen.TesteObExcelFuerDasSchreibenGeschlossenIst import \
    TesteObExcelFuerDasSchreibenGeschlossenIst

from helper.Selenium_hilfs_klassen.ErstelleUndSpeicherScreenshot import ErstelleUndSpeicherScreenshot


class TestCaseKonfiguration:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [20.09.2023]
    ####################################################################################################################
    """

    def __init__(self,
                 driver,
                 release_name,
                 test_suite_name,
                 test_name,
                 test_ausfuerungs_tabelle,
                 test_ausfuerungs_tabelle_tab_name
                 ):
        self.driver = driver

        current_path_obj = LeseAbsPfadVonDateienUndOrdnern()

        xlsx_pfad = current_path_obj.get_abs_path_to_bund_id_test_lab_execution_xlsx(
            test_execution_xlsx_name=test_ausfuerungs_tabelle)

        excel_file_path = xlsx_pfad
        self.excel_checker = TesteObExcelFuerDasSchreibenGeschlossenIst(excel_file_path)

        lese_abs_pfad_von_dateien_und_ordnern = LeseAbsPfadVonDateienUndOrdnern()

        screen_shot_location = lese_abs_pfad_von_dateien_und_ordnern.get_abs_to_save_screenshots(
            release_folder_name_from_testlab=release_name,
            test_suite_name=test_suite_name,
            test_name=test_name,
        )

        self.abs_pfad_zum_test_ausfuerhungs_ordner = screen_shot_location

        self.report_ergebnis_in_xlsx = ReporteTestCaseUndStepErgebnisseInXlsx(
            driver=self.driver,
            release_name=release_name,
            test_name=test_name,
            test_ausfuerungs_tabelle=test_ausfuerungs_tabelle,
            test_ausfuerungs_tabelle_tab_name=test_ausfuerungs_tabelle_tab_name,
            abs_pfad_zum_test_ausfuerhungs_ordner=self.abs_pfad_zum_test_ausfuerhungs_ordner,

        )
        self.test_run_number = self.report_ergebnis_in_xlsx.get_test_run_nummer() # Run_X

        self.erstelle_und_speichere_screen_shot = ErstelleUndSpeicherScreenshot(
            driver=self.driver,
            abs_pfad_zum_test_ausfuerhungs_ordner=self.abs_pfad_zum_test_ausfuerhungs_ordner,
            test_run_number=self.test_run_number
        )

    def teste_ob_test_ausfuerungs_tabelle_offen_ist(self):

        return self.excel_checker.is_excel_open()

    def report_ergebnis_in_xlsx(self):

        return self.report_ergebnis_in_xlsx

    def erstelle_und_speichere_screen_shot(self):

        return self.erstelle_und_speichere_screen_shot

    def get_test_nummer(self):

        return self.test_run_number


