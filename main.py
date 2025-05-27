import time, data, helpers # <- importando

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages import UrbanRoutesPage

class TestUrbanRoutes:

    #Definindo função
    # - Use a palavra-chave 'def'
    # - Escreva o nome da função
    # - Coloque os parâmetros entre parênteses ()
    # - Termine a linha com dois-pontos:
    # - Escreva o corpo da função indentado (com recuo)

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):  # Instrução a condição verdadeira ou falsa
            print("Conectado ao servidor Urban Routes")  # Se for True exibe a mensagem especificada na tela.
        else:  # Instrução a condição verdadeira ou falsa
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")  # Se for False exibe a mensagem especificada na tela.

        # não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.add_phone_number(data.PHONE_NUMBER)
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.choose_card_as_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.enter_message_to_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_button_blanket_and_sheets()
        assert urban_routes_page.is_blanket_and_sheets_selected(), f"O interruptor do cobertor e lenços não foi alterado."
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_button_ice_cream()
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.enter_message_to_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.click_button_car_search()
        time.sleep(2) # Apenas para conseguir visualizar o teste sem que o browser feche muito rápido após concluir o teste

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()