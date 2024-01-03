import re
from _ast import pattern


class BenutzernnameInMailinatorMailFindenUndZurueckGebenElseFalse:

    def __init__(self, mailinator_email_ihr_benutzername_text):

        self.input_string = mailinator_email_ihr_benutzername_text

    def extract_username(self):

        # Regular expression pattern to match the username
        pattern = r"Ihr Benutzername lautet: (\w+)"

        # Search for the pattern in the input string
        match = re.search(pattern, self.input_string)

        if match:
            username = match.group(1)  # Extract the matched username
            return username
        else:
            return None

if __name__ == '__main__':

    # String aus der E-Mail [Ihr Benutzername lautet]
    input_string = "Ihr Benutzername lautet: auto_user_01"

    extractor = BenutzernnameInMailinatorMailFindenUndZurueckGebenElseFalse(input_string)
    username = extractor.extract_username()
    print(username)
