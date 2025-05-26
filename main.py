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

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_fill_phone_number(self):
        #Adicionar em S8
        print("função criada para preencher o número de telefone")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.choose_comfort_car(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.choose_card_as_payment_method(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):
        #Adicionar em S8
        print("função criada para definir comentário ao motorista")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    def test_order_blanket_and_handkerchiefs(self):
        #Adicionar em S8
        print("função criada para definir cobertor e lenços")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    def test_order_2_ice_creams(self):
        #Adicionar em S8
        print("função criada para selecionar 2 sorvetes")  # Exibe a mensagem especificada na tela.
        for i in range(0, 2): # Definição do ciclo, iterar duas vezes
            pass  # 'pass' indica que a função ainda não faz nada

    def test_car_search_model_appears(self):
        #Adicionar em S8
        print("função criada para definir o modelo de busca de carro")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()