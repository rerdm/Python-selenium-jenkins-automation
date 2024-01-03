class LeseMethodenEinerKlasse:

    """
     ####################################################################################################################
     Autor: [Rene Erdmann]
     Erstellt am: [20.06.2023]
     Klasse: [ErstelleZeitstempelAlsString]
     Methoden: [is_builtin_method, inspect_methods, execute_methods]
     Funktion:
     Mit dieser Klasse ist es Möglich die Methoden einer Klasse aus zu lesen.
     Zunächst wird die Klasse instanziiert und der Klasse wird die Klasse übergeben deren Methoden ausgelesen werden
     sollen. Die Methoden werden in einem Array gespeichert.
     Mit der Methode und eine Mit der methode [execute_methods] können die Methoden
     ####################################################################################################################
     """

    def __init__(self, classes, **kwargs):
        self.classes = classes
        self.methods = []
        self.params = kwargs

    def is_builtin_method(self, method_name):
        builtin_methods = dir(object)
        return method_name in builtin_methods

    def inspect_methods(self):
        methods = [method for method in dir(self.classes) if callable(getattr(self.classes, method))]
        print(f"Methoden in Klasse '{self.classes.__name__}':")
        for method in methods:
            if not self.is_builtin_method(method):
                print(" - ", method)
                self.methods.append(method)

        return self.methods

    # def execute_methods(self, method_name, *args, **kwargs):
    #
    #     if method_name in self.methods:
    #         instance = self.classes(**self.params)
    #         method = getattr(instance, method_name)
    #         method(*args, **kwargs)
    #
    #     else:
    #         raise ValueError(f"Die Methode '{method_name}' existiert nicht.")

# Test Klassen #########################################################################################################

class MyClass:

    def __int__(self, driver, abs_pfad_zum_test_set_aufuerhungs_ordner,  webdriver_wait=20 ):
        self.driver = driver
        self.abs_pfad_zum_test_set_aufuerhungs_ordner = abs_pfad_zum_test_set_aufuerhungs_ordner
        self.webdriver_wait=webdriver_wait
    def method1(self, test_paramter_uebergabe_1):
        print(f"Method 1 called {test_paramter_uebergabe_1}")

    def method1(self, test_paramter_uebergabe_2):
        print(f"Method 1 called {test_paramter_uebergabe_2}")


if __name__ == '__main__':

    # Beispielverwendungen
    # Auslesen der Methoden einer Klasse
    lese_methoden_einer_klasse = LeseMethodenEinerKlasse(MyClass, abs_pfad_zum_test_set_aufuerhungs_ordner="test",webdriver_wait=20)

    # In dem Array werden die Methoden der Klasse gespeichert
    methods = lese_methoden_einer_klasse.inspect_methods()




