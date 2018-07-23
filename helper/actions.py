from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.touch_actions import TouchActions
import pyautogui
import time
import os
import pytesseract
from PIL import Image


#  Classe responsável por trazer as funcionalidades básicas essenciais do Selenium, visando facilitar a automação WEB e Mobile.
#  É utilizada como base principal para seguir o padrão PAGE OBJECT e NUNCA será instanciada.

class actions():

    def __init__(self, driver):
        # Objetivo: Receber um driver para poder utilzar as funções do selenium.
        self.driver = driver

    def captura(self, imagem):
        # Objetivo: Gerar e armazenar screenshots do estado atual do driver nos casos de sucesso.
        # Parametros: Recebe o nome que o screenshot será salvo.
        self.driver.get_screenshot_as_file(
            './report/sucesso/{}.PNG'.format(imagem))

    def captura_erro(self, imagem):
        # Objetivo: Gerar e armazenar screenshots do estado atual do driver nos casos de erro.
        # Parametros: Recebe o nome que o screenshot será salvo.
        self.driver.get_screenshot_as_file(
            './report/erros/{}.PNG'.format(imagem))

    def lista_selecao_em_massa(self, item, texto):
        # Objetivo: preencher todos os elementos do tipo select presentes em um elemento ou uma página inteira
        # Parametros: Recebe um elemento maior (Ex.: divs, spans, tables) e busca dentro desse item todos os selects
        #  Através do parametro texto tenta preencher todos os elementos.
        lista_de_elementos = item.find_elements_by_tag_name('select')
        for elemento in lista_de_elementos:
            try:
                self.escolhe_opcao2(elemento, texto)
            except:
                pass

    def lista_clica_em_massa(self, item, tag):
        # Objetivo: Clicar em todos os elementos presentes em um elemento maior.
        # Parametros: Recebe um elemento maior (item) e busca dentro dele todos os elementos com determinada tag e tenta clicá-los
        lista_de_elementos = item.find_elements_by_tag_name(tag)
        for elemento in lista_de_elementos:
            try:
                elemento.click()
            except:
                pass

    def lista_escrita_em_massa(self, item, tag, texto):
        # Objetivo: Preencher todos os elementos presentes em um elemento maior.
        # Parametros: Recebe um elemento maior (item) busca com base na tag e escreve o que consta no parametro texto.
        lista_de_elementos = item.find_elements_by_tag_name(tag)
        for elemento in lista_de_elementos:
            try:
                elemento.clear()
                elemento.send_keys(texto)
            except:
                pass

    def escrita_em_massa(self, tag, texto):
        # Objetivo: Tentar Preencher qualquer elemento presente na página sem necessidade de um elemento maior.
        # Parametros: A tag do elemento desejado e o texto que será escrito.
        lista_de_elementos = self.encontra_elementos(tag)
        for elemento in lista_de_elementos:
            try:
                elemento.clear()
                elemento.send_keys(texto)
            except:
                pass

    def lista_clica_por_texto(self, item, tag, texto):
        # Objetivo: Clicar no primeiro elemento com base no texto presente em seu conteúdo
        # Parametros: Elemento maior para focalizar a busca, a tag do elemento em especifico e o texto procurado
        lista_de_elementos = item.find_elements_by_tag_name(tag)
        for elemento in lista_de_elementos:
            resultado = elemento.text
            if(resultado.upper() == texto.upper()):
                elemento.click()
                break

    def encontra_por_texto(self, tag, texto):
        # Objetivo: Criar e retornar uma lista de elementos com base no texto presente em seu conteúdo
        # Parametros: Elemento a tag do elemento em especifico e o texto procurado
        lista_de_elementos = self.encontra_elementos(tag)
        lista = []
        for elemento in lista_de_elementos:
            resultado = elemento.text
            if(resultado.upper() == texto.upper()):
                lista.append(elemento)
        return lista

    def clica_por_texto(self, tag, texto):
        # Objetivo: Buscar todos os elementos e clicar com base no conteúdo
        # Parametros: a tag serve para criação da lista e o texto como condição para execução do clique.
        lista_de_elementos = self.encontra_elementos(tag)
        for elemento in lista_de_elementos:
            resultado = elemento.text
            if(resultado.upper() == texto.upper()):
                elemento.click()
                break

    def aguarde3(self, elemento, tempo=20):
        # Objetivo: Aguarda a presença de um elemento com base na sua classe.
        element = WebDriverWait(self.driver, tempo).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, elemento)))
        return element

    def aguarde2(self, elemento, tempo=20):
        # Objetivo: Aguarda a presença de um elemento com base na sua XPATH.
        element = WebDriverWait(self.driver, tempo).until(
            expected_conditions.presence_of_element_located((By.XPATH, elemento)))
        return element

    def aguarde4(self, elemento, tempo=20):
        # Objetivo: Aguarda a visibilidade de um elemento com base no seu ID.
        element = WebDriverWait(self.driver, tempo).until(
            expected_conditions.visibility_of_element_located((By.ID, elemento)))
        return element

    def aguarde(self, elemento, tempo=20):
        # Objetivo: Aguarda a presença de um elemento com base no seu ID.
        element = WebDriverWait(self.driver, tempo).until(
            expected_conditions.presence_of_element_located((By.ID, elemento)))
        return element

    def aguarde_ser_clicavel(self, elemento, tempo=60):
        # Objetivo: Aguarda um elemento ser clicavel com base no seu ID.
        element = WebDriverWait(self.driver, tempo).until(
            expected_conditions.element_to_be_clickable((By.ID, elemento)))
        return element

    def aguarde_desaparecer(self, tempo=60):
        # Objetivo: Aguarda o elemento de Carregamento desaparecer.
        warning = 'ui-dialog-title-j_idt7'
        WebDriverWait(self.driver, tempo).until(
            expected_conditions.invisibility_of_element_located((By.ID, warning)))

    def escreve(self, elemento, conteudo):
        # Objetivo: Escreve um determinado conteudo dentro de um elemento.
        e = self.encontra(elemento)
        e.send_keys(conteudo)

    def escolhe_opcao2(self, elemento, opcao, tempo=1):
        # Objetivo: Escolher uma opcao dentro de um elemento do tipo Select, porém neste método passamos
        # um objeto do tipo WebElement.
        selecao = Select(elemento)
        try:
            selecao.select_by_value(opcao)
        except Exception:
            selecao.select_by_index(opcao)
            try:
                selecao.first_selected_option
            except Exception:
                Exception

    def escolhe_opcao(self, elemento, opcao, tempo=1.2):
        # Objetivo: Escolher uma opcao dentro de um elemento do tipo Select.
        # Parametros: A informação da classe ou id do elemento Select (elemento), a opção desejada (opcao)
        warning = 'ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix'
        WebDriverWait(self.driver, 20).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, warning)))
        selecao = Select(self.encontra(elemento))
        try:
            selecao.select_by_value(opcao)
        except Exception:
            selecao.select_by_index(opcao)
            try:
                selecao.first_selected_option
            except Exception:
                Exception
        time.sleep(tempo)

    def clica(self, elementos):
         # Objetivo: Clicar em varios elementos.
         # Parametros: recebe uma string no padrao 'elemento, elemento2, elemento3' onde o separado será virgula.
         # O conteúdo da string, pode ser class, id, xpath não precisa ser do mesmo tipo.
        lista = elementos.split(', ')
        for elemento in lista:
            e = self.encontra(elemento)
            e.click()

    def clicar_atraves_de_interacao(self, tipo_elemento, texto):
        # Método repetido
        elementos = self.encontra_elementos(tipo_elemento)
        for elemento in elementos:
            if(elemento.text == texto):
                elemento.click()
                break

    def encontra_elementos(self, elemento):
        # Objetivo: Encontrar e Gerar uma lista de elementos com base numa tag passada e retorna essa lista
        e = self.driver.find_elements_by_tag_name(elemento)
        return e

    def encontra(self, elemento):
        # Objetivo: Realizar todas as tentativas necessárias (ou a maior parte delas) para encontrar um elementos.
        # Parametros: recebe uma string e retorna o elemento, caso não encontre retornará None
        e = None
        try:
            e = self.driver.find_element_by_id(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_name(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_class_name(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_xpath(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_link_text(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_tag_name(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_partial_link_text(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_css_selecor(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_binding(elemento)
        except Exception:
            pass
        try:
            e = self.driver.find_element_by_model(elemento)
        except Exception:
            pass
        return e

    def encerrar(self):
        # Objetivo: Fechar o navegador
        self.driver.close()
        try:
            os.system("TASKKILL /IM Winium.Desktop.Driver.exe")
        except Exception:
            pass

    def pegar_texto(self, elemento):
        # Objetivo: Obter um texto de um elemento
        try:
            e = self.encontra(elemento)
            return e.text
        except Exception:
            print('nenhum elemento foi especificado')

    def confirmar(self, element):
        # Objetivo: Enviar um submit para um elemento
        try:
            element.submit()
        except:
            print('Nenhum elemento foi encontrado')

    def url_atual(self):
        # Objetivo: Retorna a URL do SITE
        return self.driver.current_url

    def pagina(self, url):
        # Objetivo: Navegar para alguma página
        self.driver.get(url)

    def maximiza(self):
        # Objetivo: Maximiza o navegador
        self.driver.maximize_window()

    def atualizar(self):
        # Objetivo: Atualiza o navegador
        self.driver.refresh()

    def voltar(self):
        # Objetivo: voltar para a pagina anterior
        self.driver.back()

    def pegar_atributo(self, element, info):
        # Objetivo: Obtem atributo de um elemento
        element.get_attribute(info)

    def pegar_propriedade(self, element, info):
        # Objetivo: Obtem a propriedade de um elemento
        element.get_property(info)

    def limpar(self, element):
        # Objetivo: Limpar um campo
        element.clear()

    def titulo(self):
        # Objetivo: Retorna o titulo do navegador
        return self.driver.title

    def navegador(self):
        # Objetivo: Retonar o nome do navegador
        return self.driver.name

    def ler_imagem(self, imagem):
        # Objetivo: Le o texto de uma imagem (imagem = path da imagem)
        img = Image.open(imagem)
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        print(pytesseract.image_to_string(img))
