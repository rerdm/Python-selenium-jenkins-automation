import logging


class ErstelleUrlMitPasswortUndUsername:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: []
    Klasse: [CreateAuthenticationUrl]
    Methoden: [get_authenticated_url]
    Staus [FINAL]
    Funktion:
    Diese Klasse ermöglicht es einen Validen authorising-Url zusammenzubauen.
    Der neue Url wird dann über die Methode get_authenticate_url zurück gegeben.
    ####################################################################################################################
    """
    def __init__(self, url, username, password):

        self.url = url.replace("https://","")
        self.username = username
        self.password = password


    def gebe_authentifizierten_url_zurück(self):

        autheticate_url = "https://"+self.username+":"+self.password+"@"+self.url
        #print(autheticate_url)
        return autheticate_url

if __name__ == '__main__':

    # Beispielnutzung
    x = ErstelleUrlMitPasswortUndUsername(
        url="postfachtool-ewg.pre.buergerserviceportal.de",
        username="ewg",
        password="pCB8PoLn5tX!GnP6Xgkw"
    )

    print(x.gebe_authentifizierten_url_zurück())
    # https://ewg:pCB8PoLn5tX!GnP6Xgkw@postfachtool-ewg.pre.buergerserviceportal.de
    # https://zbp:y0hh=3/o4KU*hf0@samltool2-ewg.pre.buergerserviceportal.de/


    # Beispielnutzung
    x = ErstelleUrlMitPasswortUndUsername(
        url="samltool2-ewg.pre.buergerserviceportal.de/",
        username="ewg",
        password="y0hh=3/o4KU*hf0"
    )
    print(x.gebe_authentifizierten_url_zurück())

