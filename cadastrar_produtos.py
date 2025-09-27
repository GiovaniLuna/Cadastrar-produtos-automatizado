import pyautogui
import time
import pandas

# Passo 1: Abrir google chrome
pyautogui.PAUSE = 0.25
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2.5) 
pyautogui.press("tab") #Nesse exemplo, essa parte do código serve para selecionar um usuário do google
pyautogui.press("enter") #Se a função de escolher um usuário do google estiver inativa, essa parte do código deve ser descartada


# Passo 2: Entrar no site da empresa
'''
Nesse exemplo, está sendo utilizado o site de uma empresa hipotética
Site de exemplo disponibilizado pelo canal hashtag Programação: https://dlp.hashtagtreinamentos.com/python/intensivao/login
'''

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5) #Tempo para o site carregar

# Passo 3: Fazer login no site da empresa
pyautogui.press("tab")
pyautogui.write("usuario@gmail.com") # E-mail hipotético usado como exemplo
pyautogui.press("tab")
pyautogui.write("senhagenerica") # Senha hipotética, usada como exemplo
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 4: Retirando as informações dos produtos
tabela = pandas.read_csv("produtos.csv")
x = tabela["codigo"]
print(x)

# Passo 5: Adicionando todos os produtos no site
pyautogui.press("tab")
for linha in tabela.index:
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    for i in range(0,7): # Volta para o primeiro campo de cadastrar produto
        pyautogui.hotkey("shift","tab") 



