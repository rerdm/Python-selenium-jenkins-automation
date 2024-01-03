
class IncreaseTestCaseNumber:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: []
    Klasse: []
    Methoden: []
    Staus [FINAL]
    Funktion:


    ####################################################################################################################
    """
    def __init__(self, test_step_number):
        self.number = test_step_number

    def increase_number(self):
        self.number += 0.1
        return round(self.number, 1)

if __name__ == '__main__':

    increaser = IncreaseTestCaseNumber(test_step_number=1)
    print(increaser.increase_number())
    print(increaser.increase_number())
    print(increaser.increase_number())

