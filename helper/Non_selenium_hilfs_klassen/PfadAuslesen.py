
import inspect
import os

class PfadAuslesen:

    def __init__(self):
        self.current_directory = os.getcwd()
        self.new_path = []

    def get_pfad_zum_test_lab_ordner(self):

        elements = self.current_directory.split("\\")

        for index, element in enumerate(elements):
            self.new_path.append(element)
            if index == 4:  # Beende die Schleife nach der dritten Iteration (Index beginnt bei 0)
                break

        result = '/'.join(self.new_path)
        return result+"/"


if __name__ == "__main__":
    # Beispielaufruf der Klasse
    current_dir_holder = PfadAuslesen()
    pfad_zum_test_lab_ordner = current_dir_holder.get_pfad_zum_test_lab_ordner()
    print("pfad_zum_test_lab_ordner:", pfad_zum_test_lab_ordner)
