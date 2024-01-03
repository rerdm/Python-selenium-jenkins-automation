import time


class GebeCountDownInCmdAus:
    @staticmethod
    def starte_countdown(schritt,countdown_in_sekunden,kommentar=None):

        while countdown_in_sekunden > 0:

            minutes = countdown_in_sekunden // 60
            remaining_seconds = countdown_in_sekunden % 60

            if kommentar:
                countdown_format = '\r {} - Schritt [{}] - Verbleibende Zeit: {:2d} Minuten {:02d} Sekunden'.format(kommentar,schritt, minutes, remaining_seconds)
                print(countdown_format, end='')
            else:
                countdown_format = '\r Schritt [{}] - Verbleibende Zeit: {:2d} Minuten {:02d} Sekunden'.format(schritt, minutes, remaining_seconds)
                print(countdown_format, end='')

            time.sleep(1)
            countdown_in_sekunden -= 1

        #print('\nCountdown abgelaufen!')

if __name__ == '__main__':

    # Hier rufst du die statische Methode der Klasse auf und übergibst die gewünschte Z
    # eit in Sekunden (300 in diesem Fall)

    GebeCountDownInCmdAus.starte_countdown(
        schritt=1,
        countdown_in_sekunden=5,
        kommentar="optionaler parameter dient zur genaueren Beschreibung"  # Optional
    )

