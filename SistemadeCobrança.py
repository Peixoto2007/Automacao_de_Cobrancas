
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import json

webbrowser.open('https://web.whatsapp.com/')
sleep(20)
workbook = openpyxl.load_workbook('zapbot.xlsx')
planilhaclientes= workbook['Planilha1']
for linha in planilhaclientes.iter_rows(min_row=2):
    #nome, telefone.
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    print(nome) 
    print(telefone)
    print(vencimento)
    mensagem = f"Estou testando , seu boleto vai vencer {vencimento} pague no pix = ******"
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
    webbrowser.open(link)                                                                                   
    sleep(20)
    try:
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey('ctrl','w')
        sleep(30) # vamo evitar o bloqueio kk
    except:
        print(f"Nao foi possivel enviar a mensagem ")
        with open ('erros.csv',"a",newline='') as arquivo:
            arquivo.write(f"{nome,}{telefone}")