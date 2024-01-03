

class SwitchToDriverHandle:
    def __init__(self, driver):

        self.driver = driver

    def switch_to_handle_number(self, handle_number):

        self.driver.switch_to.window(self.driver.window_handles[handle_number])

    def switch_to_default_handle_number(self, handle_number):

        self.switch_to_handle_number(handle_number=handle_number)

    def zeige_mir_alle_window_handles_an(self):

        handle_number = 0
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # Mit dieser Methode können die Aktuellen handels ausgegeben werden
            # print(f"Driver Handle [{handle_number}] Title : {self.driver.title}")
            handle_number += 1









