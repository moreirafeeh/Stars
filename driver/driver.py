from selenium import webdriver
import os

class WebDriverBuilder():
    
    def __init__(self, site):
        # Esta classe irá retornar um driver do Chrome e no seu construtor será passado a URL inicial de navegacao.

        self.driver = webdriver.Chrome('{}/bin/chromedriver.exe'.format(os.getcwd()))
        self.driver.get('http://' + site)

    def get_driver(self):
        # Use este método para obter o Driver e utilizá-lo no padrão PAGE OBJECT.
        return self.driver