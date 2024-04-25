import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=973, y=426)
pyautogui.write("meu_login")

tabela = pd.read_csv(r"C:\Users\leozi\Downloads\Compras.csv")
print(tabela)

total_gasto = tabela["ValorFinal"].sum() # os colchetes nesse caso serve para puxar o nome de uma coluna
quantidade = tabela["Quantidade"].sum()
preco_media = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_media)
