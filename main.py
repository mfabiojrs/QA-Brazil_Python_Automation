import data, helpers # <- importando
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


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
        #Adicionar em S8
        print("função criada para definir a rota")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    def test_select_plan(self):
        #Adicionar em S8
        print("função criada para selecionar o plano")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    def test_fill_phone_number(self):
        #Adicionar em S8
        print("função criada para preencher o número de telefone")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

    def test_fill_card(self):
        #Adicionar em S8
        print("função criada para preencher o cartão")  # Exibe a mensagem especificada na tela.
        pass  # 'pass' indica que a função ainda não faz nada

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