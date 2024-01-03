import os

class LeseAbsPfadVonDateienUndOrdnern:
    @staticmethod
    def get_abs_path_to_bund_id_project():

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "/".join(new_path)
        return new_path+"/"
    @staticmethod
    def get_abs_path_to_bundID_test_plan():

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "/".join(new_path)
        new_path = new_path+"/Test_Plan/"

        return new_path

    @staticmethod
    def get_abs_path_to_bund_id_test_lab():

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "/".join(new_path)
        new_path = new_path+"/Test_Lab/"

        return new_path

    @staticmethod
    def get_abs_path_to_bund_id_test_lab():

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "/".join(new_path)
        new_path = new_path+"/Test_Lab/"

        return new_path

    @staticmethod
    def get_abs_path_to_bund_id_test_lab_execution_xlsx(
            test_execution_xlsx_name
    ):

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "/".join(new_path)
        new_path = new_path+"/Test_Lab/"+test_execution_xlsx_name

        return new_path


    @staticmethod
    def get_abs_to_save_screenshots(
            release_folder_name_from_testlab, test_suite_name, test_name
    ):

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "/".join(new_path)
        new_path2 = f"{new_path}/Test_Lab/{release_folder_name_from_testlab}/{test_suite_name}"
        new_path = f"{new_path}/Test_Lab/{release_folder_name_from_testlab}/{test_suite_name}/{test_name}"

        # Erstellen des Test-Suite-Ordners.
        try:
            os.makedirs(new_path2, exist_ok=True)
        except:
            print(f"ERROR - Ordner konnte nicht erstellt werde PFAD: {new_path2}")

        # Erstellen des Test-Case-Ordners.
        try:
            os.makedirs(new_path, exist_ok=True)
        except:
            print(f"ERROR - Ordner konnte nicht erstellt werde PFAD: {new_path}")

        return new_path


    @staticmethod
    def get_abs_zu_den_elster_zertifikaten():

        new_path = []
        path = os.path.abspath(os.path.dirname(__file__)).split("\\")

        for i in range(len(path)-2):
            new_path.append(path[i])

        new_path = "\\".join(new_path)
        new_path = f"{new_path}\\Utils\\Elster_Zertfifikate\\"

        return new_path


if __name__ == "__main__":

    current_path_obj = LeseAbsPfadVonDateienUndOrdnern()
    elster_pfad = current_path_obj.get_abs_zu_den_elster_zertifikaten()

    abs_pfad_zum_bund_id_projekt = current_path_obj.get_abs_path_to_bund_id_project()
    print("abs_pfad_zum_bund_id_projekt:", abs_pfad_zum_bund_id_projekt)

    abs_pfad_zum_bund_id_test_plan = current_path_obj.get_abs_path_to_bundID_test_plan()
    print("abs_pfad_zum_bund_id_test_plan:", abs_pfad_zum_bund_id_test_plan)

    abs_pfad_zum_bund_id_test_lab = current_path_obj.get_abs_path_to_bund_id_test_lab()
    print("get_abs_path_to_bund_id_test_lab:", abs_pfad_zum_bund_id_test_lab)

    abs_pfad_zum_bund_id_test_lab_release_07 = current_path_obj.get_abs_path_to_bund_id_test_lab()
    print("abs_pfad_zum_bund_id_test_lab_release_07:", abs_pfad_zum_bund_id_test_lab_release_07)

    abs_pfad_zum_bund_id_test_lab_release_07 = current_path_obj.get_abs_path_to_bund_id_test_lab()
    print("abs_pfad_zum_bund_id_test_lab_release_07:", abs_pfad_zum_bund_id_test_lab_release_07)

    elster_pfad = current_path_obj.get_abs_zu_den_elster_zertifikaten()
    print("elster_pfad:", elster_pfad)


    abs_path_to_bund_id_test_lab_release_07_test_fall_ergebnisse_xlsx = current_path_obj.get_abs_path_to_bund_id_test_lab_execution_xlsx(
            test_execution_xlsx_name="Bund_id_Testfall_ausführung.xlsx",
        )

    test_name = "001 - Registrierung- mit Elster - Positivtest"
    test_suite_name = "08_Elster"

    screen_shot_location = current_path_obj.get_abs_to_save_screenshots(
        release_folder_name_from_testlab="Release_7_0",
        test_suite_name=test_suite_name,
        test_name=test_name
    )
    print("screen_shot_location",screen_shot_location)
    print("abs_path_to_bund_id_test_lab_release_07_test_fall_ergebnisse_xlsx:", abs_path_to_bund_id_test_lab_release_07_test_fall_ergebnisse_xlsx)



