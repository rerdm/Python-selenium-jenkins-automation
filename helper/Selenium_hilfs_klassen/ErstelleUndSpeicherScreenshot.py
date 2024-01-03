import inspect
import logging
import sys
import time


class ErstelleUndSpeicherScreenshot:
    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [17.07.2023]
    Klasse: [ErstelleUndSpeicherScreenshot]
    ####################################################################################################################
    """

    def __init__(self, driver, abs_pfad_zum_test_ausfuerhungs_ordner, test_run_number):

        self.action = None
        self.driver = driver
        self.test_run_number = test_run_number

        self.abs_pfad_zum_test_ausfuerhungs_ordner = abs_pfad_zum_test_ausfuerhungs_ordner


    def einzelner_screenshot_der_webseite(self,
                                          step_number,
                                          screen_shot_name=None,
                                          ):

        class_name = self.__class__.__name__
        method_name = inspect.currentframe().f_code.co_name

        # Ausgabe des Klassen- und Methodennamens
        # print("# Screenshot Erstellung -------------------------------------------------------------------------------"
        #       "----------- ")
        # print("Klasse.methode                               : "+class_name+"."+method_name)
        # print("step_number                                  :", step_number)

        try:
            step_number = int(step_number.replace("Step ",""))
        except:
            pass

        test_run = "/RUN_"+self.test_run_number

        # Prüfen, ob die Step number eine einzelne Zahl ist
        if step_number == "Vorbedingungen":
            # print("EINZELNER SCREEN SHOT INT  - NAME :", screen_shot_name)
            action = screen_shot_name.upper()
            # print(" - INT - screenshot_vor_der_aktion :", screen_shot_name)
            abs_pfad_plus_screen_shot_name = self.abs_pfad_zum_test_ausfuerhungs_ordner + "/"+test_run+"_1_" + str(
                step_number) + "_" + action + ".png"
            full_screen_shot_name = test_run+"_1_" + str(step_number) + "_" + action + ".png"

        # Prüfen, ob die Step number eine einzelne Zahl ist
        if type(step_number) == int:
            # print("EINZELNER SCREEN SHOT INT  - NAME :", screen_shot_name)
            action = screen_shot_name.upper()
            # print(" - INT - screenshot_vor_der_aktion :", screen_shot_name)
            abs_pfad_plus_screen_shot_name = self.abs_pfad_zum_test_ausfuerhungs_ordner + "/"+test_run+"_Step_" + str(
                step_number) + ".0_" + action + ".png"
            full_screen_shot_name = test_run+"_Step_" + str(step_number) + ".0_" + action + ".png"

        if type(step_number) == float:

            # print("EINZELNER SCREEN SHOT FLOAT - NAME :", screen_shot_name)
            if screen_shot_name:
                # print(" - FLOAT - screen_shot_name :", screen_shot_name)
                action = screen_shot_name.upper()
                abs_pfad_plus_screen_shot_name = self.abs_pfad_zum_test_ausfuerhungs_ordner + "/"+test_run+"_Step_" + str(
                    step_number) + "_" + action +".png"
                full_screen_shot_name = test_run+"_Step_" + str(step_number) + "_" + action +".png"

        # print("Screenshot name                              :", full_screen_shot_name.replace("/",""))
        # print("Erstellter Screenshot im pfad                :", abs_pfad_plus_screen_shot_name)

        self.driver.save_screenshot(abs_pfad_plus_screen_shot_name)

