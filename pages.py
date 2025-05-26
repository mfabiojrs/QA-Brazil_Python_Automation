from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code


class UrbanRoutesPage:

    # Localizadores, atributos de classe/elementos
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    RACE_LOCATOR = (By.CSS_SELECTOR, '.button.round')
    SELECT_COMFORT_LOCATOR = (By.CSS_SELECTOR, '.tcard-icon')

    PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, '.np-button')
    PHONE_NUMBER = (By.ID, 'phone')
    SUBMIT_PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, '.button.full')
    SMS_CODE = (By.ID, 'code')

    PAYMENT_METHOD_LOCATOR = (By.CSS_SELECTOR, '.pp-button.filled')
    CARD_METHOD_LOCATOR = (By.CSS_SELECTOR, '.pp-row.disabled')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.CSS_SELECTOR, '.card-code-input #code')
    CARD_NUMBER_LABEL = (By.CSS_SELECTOR, '.card-number-label')
    BUTTON_ADD_LOCATOR = (By.CSS_SELECTOR, '.pp-buttons button[type="submit"]')
    CLOSE_PAYMENT_METHOD_LOCATOR = (By.CSS_SELECTOR, '.close-button.section-close')

    MESSAGE_TO_DRIVER_LOCATOR = (By.CSS_SELECTOR, '.input-container #comment')

    BUTTON_COUNT_TO_ICE_CREAM = (By.CLASS_NAME, 'counter-plus')

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

    def click_phone_number(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_NUMBER_LOCATOR)).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.SUBMIT_PHONE_NUMBER_LOCATOR).click()

    def enter_sms_code(self):
        sms_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.SMS_CODE).send_keys(sms_code)

    def submit_phone_number(self):
        button = self.driver.find_elements(*self.SUBMIT_PHONE_NUMBER_LOCATOR)
        select_button = button[1]
        select_button.click()

    def add_phone_number(self, phone_number):
        self.click_phone_number()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        self.enter_sms_code()
        self.submit_phone_number()

    # Método que clica na forma de pagamento
    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    # Método que seleciona cartão como forma de pagamento
    def click_card_method(self):
        self.driver.find_element(*self.CARD_METHOD_LOCATOR).click()

    # Método que preenche o número do cartão
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    # Método que preenche o código do cartão
    def enter_card_code(self, card_code):
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(card_code)

    # Método que preenche o número e o código do cartão
    def add_card(self, card_number, card_code):
        self.enter_card_number(card_number)
        self.enter_card_code(card_code)

    # Método que clica fora do campo do cartão somente para o botão adicionar ficar ativo
    def click_card_number_label(self):
        self.driver.find_element(*self.CARD_NUMBER_LABEL).click()

    # Método que clica no botão adicionar 'cartão'
    def click_button_add_card(self):
        self.driver.find_element(*self.BUTTON_ADD_LOCATOR).click()

    # Método que fecha a forma de pagamento
    def click_close_payment_method(self):
        button = self.driver.find_elements(*self.CLOSE_PAYMENT_METHOD_LOCATOR)
        select_button = button[2]
        select_button.click()

    # Método que seleciona cartão como forma de pagamento e adiciona o cartão de crédito
    def choose_card_as_payment_method(self, card_number, card_code):
        self.click_payment_method()
        self.click_card_method()
        self.add_card(card_number, card_code)
        self.click_card_number_label()
        self.click_button_add_card()
        self.click_close_payment_method()

    # Método que preenche a mensagem para o motorista
    def enter_message_to_driver(self, message):
        self.driver.find_element(*self.MESSAGE_TO_DRIVER_LOCATOR).send_keys(message)

    # Método que clica/seleciona 2 sorvete
    def click_button_ice_cream(self):
        ice_cream = self.driver.find_element(*self.BUTTON_COUNT_TO_ICE_CREAM)
        for i in range(0, 2):
            ice_cream.click()