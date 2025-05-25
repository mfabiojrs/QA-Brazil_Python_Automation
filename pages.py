from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    # Localizadores, atributos de classe/elementos
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Espera explícita de até 10 segundos

    # Método que preenche o campo De
    def enter_from_location(self, from_text):
        self.wait.until(EC.element_to_be_clickable(self.FROM_LOCATOR)).send_keys(from_text) # # Espera explícita para que o campo carregue

    # Método que preenche o campo Para
    def enter_to_location(self, to_text):
        self.wait.until(EC.element_to_be_clickable(self.TO_LOCATOR)).send_keys(to_text) # Espera explícita para que o campo carregue

    # Método que preenche o campo De e Para
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)