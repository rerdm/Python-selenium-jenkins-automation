import random
import string

class BuchstabenGenerator:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [15.06.2023]
    Klasse: [BuchstabenGenerator]
    Methoden: [generate_string]
    Staus [FINAL]
    Funktion:
    Mit dieser Klasse kann eine Anzahl von Zufallsbuchstaben generiert werden, die Klasse kann hilfreich sein,
    um input Felder zu testen (255 Buchstaben sind gültig 266 nicht gültig )
    ####################################################################################################################
    """
    def generate_string(self, length):

        self.length_to_string = length
        random_letters = ''.join(random.choices(string.ascii_letters, k=length))
        return random_letters
    def generate_string2(self, length):

        self.length_to_string = length
        random_letters = ''.join(random.choices(string.ascii_letters, k=length))
        random_letters

if __name__ == '__main__':

    # Beispielverwendung
    generator = BuchstabenGenerator()
    random_string_with_256_letters = generator.generate_string(80)
    random_string_254 = generator.generate_string(254)
    random_string_256 = generator.generate_string(256)
    random_string_43 = generator.generate_string(42)


    print(random_string_with_256_letters)

