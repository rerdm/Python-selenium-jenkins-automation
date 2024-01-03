import logging


class LoggerKlasse:

    def logging_info_methodo_wurde_ausgefuert(self,methoden_name_als_string):

        logging.info(f"               Methode wurde ausgefuert : {methoden_name_als_string} ")

    def logging_error_fehler_in_der_methode(self,methoden_name_als_string):
        pass

    def logging_info_assertion_war_erfolgreich_erwartete_url_nach_button_klick(self,step_numer, erwarteter_url):

        logging.info(f"             {step_numer}-Step - Richtiger Url nach button click {erwarteter_url}  [PASSED]")

    def logging_info_assertion_war_erfolgreich_ewratete_url_for_test_beginn(self,step_numer, erwarteter_url):

        logging.info(f"             {step_numer}-Step - Richtiger Url vor beginn des Tests {erwarteter_url} [PASSED]")