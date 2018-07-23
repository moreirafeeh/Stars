
import time 
from helper.actions import actions


class star(actions):

    def __init__(self, driver):
        self.driver = driver

    def pesquisa(self, conteudo):
        self.escreve('lst-ib', conteudo)
        self.clica('//*[@id="tsf"]/div[2]/div[3]/center/input[1]')
   
    def logar(self, usuario, senha):
        self.escreve('//*[@id="form1:j_idt7_content"]/table[1]/tbody/tr[1]/td[2]/input',usuario)
        self.escreve('//*[@id="form1:j_idt7_content"]/table[1]/tbody/tr[2]/td[2]/input', senha)
        self.clica('//*[@id="form1:j_idt14"]') 
        time.sleep(3)   

    def buscarID(self, numero):
        self.escreve('templateForm:j_idt101', numero)
        self.clica('templateForm:j_idt102')
        time.sleep(3)

            
    def valida_titulo_pagina(self, conteudo):    
        title = self.titulo()
        assert conteudo in title

    def valida_status(self, Numfoto):
        AUMENTAR = '1'
        textoInsta = 'INSTALADO'   
        encontratexto = self.encontra('//*[@id="form:tabDetalheId"]/div[2]/table/tbody/tr[3]/td[4]') 
        converte = encontratexto.text
        assert  converte == textoInsta
        self.fotografar_pagina_final(Numfoto)
        Numfoto = Numfoto + AUMENTAR
        print(Numfoto)
        return Numfoto 
    
    def fotografar_pagina_final(self, i):
        self.captura(i)   
