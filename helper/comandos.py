import pyautogui
import time
import os
    
def clica_coordenada(x,y,vezes=1,botao='left'):
    # Objetivo: Realizar um clique de mouse com base em coordenadas.
    # Parametro: X se refere a direita (numeros positivos) ou esquerda (numeros negativos).
    # Parametro: Y se refere ao lado inferior (numeros positivos) ou superior (numeros negativos).
    pyautogui.click(x,y,clicks=vezes,button=botao)
    time.sleep(vezes)
    
def arraste_coordenada(xi,yi,xf,yf):
    # Objetivo: Realizar um evento de arraste com o mouse
    # Parametro: passar as coordenadas iniciais e as finais
    pyautogui.mouseDown(x=xi,y=yi,button='left')
    pyautogui.dragTo(x=xf,y=yf,duration=0)
    
def digitos(digito,interval = 0.3):
    # Objetivo: Realizar comandos de teclados de forma individual
    # Parametro: (digito) pode ser qualquer tecla e deve ser passado com string no padrao: ('tab, enter, f2, 4, C')
    lista = digito.split(', ')
    for elemento in lista:
        pyautogui.press(elemento, interval=interval)
    
def rolagemMouse(x):
    # Objetivo: Realizar o evento de rolagem de tela de acordo com uma coordenada
    pyautogui.scroll(x)
    
def mantenha_e_digite(mantenha,digite,vezes=1):
    # Objetivo: Realizar um comando do teclado no qual combina duas ou mais teclas, sendo que uma delas se mantem pressionada
    # Parametro: um exemplo seria o 'ctrl + c' (mantenha = 'ctrl'), (digite = 'c') e a quantidade de vezes que este comando será repetido
    pyautogui.keyDown(mantenha)
    quantidade=0
    while(quantidade!=vezes):
        digitos(digite)
        quantidade+=1
    pyautogui.keyUp(mantenha)

def press_duasTeclas(pri,seg, tempo = 0.5):
    # Objetivo: Realizar um comando do teclado no qual combina duas ou mais teclas, sendo que uma delas se mantem pressionada
    # Parametro: um exemplo seria o 'ctrl + c' (pri = 'ctrl'), (seg = 'c') e a quantidade de vezes que este comando será repetido
    pyautogui.hotkey(pri, seg)
    time.sleep(tempo)

def press_tresTeclas(pri,seg,ter):
    # Objetivo: Realizar um comando do teclado no qual combina duas ou mais teclas, sendo que uma delas se mantem pressionada
    # Parametro: um exemplo seria o 'ctrl + alt + del' (pri = 'ctrl'), (seg = 'alt'), (tri = 'del') e a quantidade de vezes que este comando será repetido
    pyautogui.hotkey(pri,seg,ter)

def clica_imagem(imagem,clicks=1,botao='left'):
    # Objetivo: Clica numa imagem na tela com base nos arquivos presentes em "bin/imagens"
    # Parametro: Recebe o nome do arquivo que consta na pasta "bin/imagens"
    diretorio = os.getcwd() + '/bin/imagens/'
    x,y=pyautogui.locateCenterOnScreen(diretorio + imagem + '.PNG')
    pyautogui.click(x,y,clicks=clicks,button=botao)

def escrever_direto(conteudo):
    # Objetivo: Escreve um conteúdo de forma direta independente do posicionamento do cursor do mouse
    pyautogui.typewrite(conteudo)

def tab(vezes = 1):
    # Objetivo: Realizar o comando de Tab
    rodadas = 0
    while(rodadas < vezes):
        pyautogui.press("tab", interval = 0.1)
        rodadas += 1

def aguarde_tela(imagem, comando = None, score=50, valida = True):
    # Objetivo: Aguardar que uma imagem apareça na tela e retornar as coordenadas dessa imagem.
    # Ele tentara 50 vezes encontrar a imagem e retornará None em caso de falha. 
    # Parametros: É possivel realizar um comando enquanto a imagem não aparece
    pontos = 0
    resultado = 1
    while(pyautogui.locateOnScreen('{}/bin/imagens/{}.PNG'.format(os.getcwd(), imagem)) is None):
        if(comando is not None):
            digitos(comando)
        resultado = 1
        pontos += 1
        if(pontos > score):
            resultado = 2
            break
    if(valida):
        assert resultado == 1
    return pyautogui.locateOnScreen('{}/bin/imagens/{}.PNG'.format(os.getcwd(), imagem))