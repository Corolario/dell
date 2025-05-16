import time
import datetime
import asyncio
from telegram import Bot
from playwright.sync_api import sync_playwright

url = "https://www.dell.com/pt-br/outlet/shop"
intervalo=60

async def envia_msg(mensagem):
    bot = Bot(token='7977985:AAFkcNNXNaGSNno9DoLCiJQ')
    chat_id = '7234221214'
    await bot.send_message(chat_id=chat_id, text=mensagem)

def download_webpage(url):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        html_content = page.content()
        browser.close()
        return html_content

def verificacao():
    html = download_webpage(url)
    with open("conteudo.txt", "r") as arquivo:
        conteudo_anterior = arquivo.read()
    if html != conteudo_anterior:
        agora = datetime.datetime.now()
        mensagem = f"{agora.strftime('%d/%m/%Y %H:%M:%S')} - A pagina foi alterada!"
        asyncio.run(envia_msg(mensagem))
        with open("conteudo.txt", "w") as arquivo:
            arquivo.write(html)

while True:
    verificacao()
    time.sleep(intervalo)
