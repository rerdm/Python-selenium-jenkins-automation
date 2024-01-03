


class BundID_bn_anmelden_konto_aktivitaeten_lokatoren_js:

        PASSWORT_WURDE_ERFOLGREICH_ZURUECK_GESETZT_LETZTER_EINTRAG = """
            var trElements = document.querySelectorAll("tr");
            var message = "";
            for (let i = 0; i < trElements.length; i++) {
                if (trElements[i].textContent.includes("Passwort wurde erfolgreich zurückgesetzt.")) {
                    message = trElements[i].textContent;
                    break;
                }
            }
            return message;
        """

        ANMELDUNG_MIT_BENUTZERNAME_UND_PASSWORT_NACHRICHT = """
            var trElements = document.querySelectorAll("tr");
            var message = "";
            for (let i = 0; i < trElements.length; i++) {
                if (trElements[i].textContent.includes("Anmeldung mit Benutzername & Passwort.")) {
                    message = trElements[i].textContent;
                    break;
                }
            }
            return message;
        """

        KONTO_WURDE_ERSTELLT_NACHRICHT = """
            var trElements = document.querySelectorAll("tr");
            var message = "";
            for (let i = 0; i < trElements.length; i++) {
                if (trElements[i].textContent.includes("Konto wurde erstellt.")) {
                    message = trElements[i].textContent;
                    break;
                }
            }
            return message;
        """

        SITZUNG_IST_ABGELAUFEN_AUTOMATISCHE_ABMELDUNG_ERFOLGT_NACHRICHT = """
            var trElements = document.querySelectorAll("tr");
            var message = "";
            for (let i = 0; i < trElements.length; i++) {
                if (trElements[i].textContent.includes("Sitzung ist abgelaufen. Abmeldung ist erfolgt.")) {
                    message = trElements[i].textContent;
                    break;
                }
            }
            return message;
        """
