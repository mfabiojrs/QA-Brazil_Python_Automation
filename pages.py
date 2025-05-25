from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    # Localizadores, atributos de classe/elementos
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    RACE_LOCATOR = (By.CSS_SELECTOR, '.button.round')
    SELECT_COMFORT_LOCATOR = (By.CSS_SELECTOR, '.tcard-icon')

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

    # Método que seleciona a corrida comfort
    def choose_comfort_car(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.wait.until(EC.element_to_be_clickable(self.RACE_LOCATOR)).click()
        choose_car_list = self.wait.until(EC.presence_of_all_elements_located(self.SELECT_COMFORT_LOCATOR))
        if len(choose_car_list) > 4:
            choose_car_list[4].click()  # Se pelo menos 5 carros, selecionar o 5º (índice 4)
        elif choose_car_list:
            choose_car_list[0].click()  # Seleciona o primeiro carro disponível se houver menos de 5
        else:
            return  # Nenhum carro disponível, não faz nada