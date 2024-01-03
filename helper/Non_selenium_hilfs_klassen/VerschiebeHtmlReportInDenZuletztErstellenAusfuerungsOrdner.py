
import os
import glob

import os
import glob

class VerschiebeHtmlReportInDenZuletztErstellenAusfuerungsOrdner:

    def __init__(self,name_des_test_set_asufuerungs_ordners_aus_dem_selben_verzeichnis):
        self.folder = None
        self.test_set_ausfuerungs_ordner = name_des_test_set_asufuerungs_ordners_aus_dem_selben_verzeichnis

    def finde_den_zuletzt_erstellten_test_ausfuerungsordner(self):
        base_dir = os.path.join(os.getcwd(), self.test_set_ausfuerungs_ordner)
        folders = glob.glob(os.path.join(base_dir, "*"))  # Alle Ordner im "Test Ergebnisse" Verzeichnis
        folders = [folder for folder in folders if os.path.isdir(folder)]  # Nur Verzeichnisse auswählen

        self.folder = max(folders, key=lambda folder: os.path.getctime(folder))

    def get_name_des_ordners(self):

        last_element = os.path.basename(self.folder)

        return last_element

if __name__ == '__main__':

    # Beispielverwendung
    folder_finder = VerschiebeHtmlReportInDenZuletztErstellenAusfuerungsOrdner()
    folder_finder.finde_den_zuletzt_erstellten_test_ausfuerungsordner()
    newest_folder = folder_finder.get_name_des_ordners()
    print("Neuester Ordner:", newest_folder)






