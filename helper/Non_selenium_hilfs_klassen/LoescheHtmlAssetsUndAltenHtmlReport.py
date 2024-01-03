

import os

class LoescheHtmlAssetsUndAltenHtmlReport:
    def __init__(self):
        pass

    def delete_folder(self, folder_path):
        try:
            os.system(f'rmdir /s /q "{folder_path}"')
        except:
            print("ERROR: Der Ordner konnte nicht gelöscht werden.\n"
                  "Der Ordner muss nach dem Testlauf manuell gelöscht werden, um Ressourcen zu sparen.")

    def delete_file(self, file_path):
        try:
            os.system(f'del "{file_path}"')
        except:
            print(f"ERROR: Die Datei '{file_path}' konnte nicht gelöscht werden.\n"
                  "Bitte manuell löschen.\n")

# Hauptprogramm
if __name__ == "__main__":

    file_deleter = LoescheHtmlAssetsUndAltenHtmlReport()

    # Löschen des 'assets'-Ordners
    file_deleter.delete_folder("assets")

    # Löschen der 'Benutzername_anfordern.html'-Datei
    file_deleter.delete_file("Benutzername_anfordern.html")
