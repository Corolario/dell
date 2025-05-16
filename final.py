import time
import datetime
from playwright.sync_api import sync_playwright

url = "http://192.168.8.58"
intervalo=60

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
        print(f"{agora.strftime('%d/%m/%Y %H:%M:%S')} - A pagina foi alterada!")
        with open("conteudo.txt", "w") as arquivo:
            arquivo.write(html)
while True:
    verificacao()
    time.sleep(intervalo)
