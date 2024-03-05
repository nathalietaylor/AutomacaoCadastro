
#criar passo a passo do projeto
# Passo 1: entrar no sistema
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
# terminal > command prompt > pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 1 #para pausa a cada comando

# abrir Chrome no site desejado
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#para comandos de 2 teclas, ex ctrl+v: pyautogui.hotkey("ctrl","v")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2) #programa irá esperar 2seg para o proximo comando


#passo 2: fazer login 
#criar arquivo auxiliar para determinar coordenadas do click

#clicar no campo de login
pyautogui.click(x=714, y=365) 
pyautogui.write("emailteste@gmail.com")

# pyautogui.click(x=714, y=465) para clicar no campo senha ou clicar tab p/ passar para o campo seguinte
pyautogui.press("tab")
pyautogui.write("teste")

#clicar no botão de logar
pyautogui.click(x=670, y=542)
time.sleep(3) #para dar tempo para carregar pág

#Passo 3: Importar base de dados
#terminal > command prompt > pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")

#Passo 4: cadastrar um produto

#para cada linha da tabela ( no pandas, linha = index)
for linha in tabela.index: 
    #clicar no primeiro campo
    pyautogui.click(x=648, y=263)
     #linha muda, mas sempre na coluna codigo
    cod = tabela.loc[linha, "codigo"]  
    pyautogui.write(cod)
    pyautogui.press("tab") 
    marca = tabela.loc[linha, "marca"]   
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]    
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #colunas categoria, preco e custo precisam entrar como texto e não numero
    categ = tabela.loc[linha, "categoria"] 
    pyautogui.write(str(categ))
    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]    
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]      
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #há linhas que não possuem obs, é necessário verificar se está vazia (isna)
    #nan = info vazia - not a number
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):   
        pyautogui.write(obs)
    #para clicar no enviar (x=597, y=649) ou tab e depois enter  
    pyautogui.press("tab")
    pyautogui.press("enter")
    #subir tela para novo cadastro, scroll para cima +, para baixo -
    pyautogui.scroll(5000) 

#Passo 5: 
