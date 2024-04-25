import pyautogui as pg
import time 
from termcolor import colored
import textwrap
import subprocess
import os

itens = []
print("Digite o texto no formato 'AAA X / AA XXX' (digite 'fim' para encerrar):")
while True:
    linha = input().strip()
    if linha.lower() == 'fim':
        break
    itens.append(linha)

caminho_arquivo = r"C:\CSV\Etiquetas.csv - colar aqui.csv (1).csv"

with open(caminho_arquivo, 'w') as arquivo:
    for item in itens:
        arquivo.write(f"{item}\n")

print(f"Lista de itens foi salva em: {caminho_arquivo}")

caminho_arquivo = r'C:\Etiquetas\Bandeja QR code\RETs e RES e AMO csv.nlbl'


os.startfile(caminho_arquivo)
 
procurando = True
while procurando:
    try:
        img = pg.locateCenterOnScreen("imagem (1).png")
        procurando = False
        print("Executanto resto do codigo")
    except:
        print("Procurando")

pg.hotkey("ctrl", "p") # Acessa a tela de impressão
time.sleep(1)

pg.press('tab')
time.sleep(0.5)

pg.press('tab')
time.sleep(0.5)

pg.press("2") #Define a velocidade de impressão
time.sleep(0.5)
pg.press("tab")
time.sleep(0.5)
pg.press("1") #Define o primeiro digito de obscuridade de impressão
pg.press("8") #Define o segundo digito de obscuridade de impressão
time.sleep(0.5)
pg.press("enter")
time.sleep(1)
pg.hotkey("alt","f4")
time.sleep(0.5)
pg.press("x")

pg.alert("Concluído com sucesso!!") 

