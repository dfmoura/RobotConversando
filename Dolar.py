import datetime

from playwright.sync_api import sync_playwright

dataAtual = datetime.date.today()

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  # headless - não demonstra o que realiza.
    pagina = navegador.new_page()
    pagina.goto("https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome..69i57j0i271l3j69i60j69i65.2529j0j1&sourceid"
                "=chrome&ie=UTF-8")
    pagina.locator('xpath=//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').dblclick()
    pagina.keyboard.press("Control+C")
    pagina.goto("https://translate.google.com/")
    pagina.wait_for_timeout(1000)
    pagina.fill('xpath=//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]'
                '/div[3]/c-wiz[1]/span/span/div/textarea', f'{dataAtual}, Olá colegas, \n'
                                                           'A cotação do Dólar agora é: ')
    pagina.keyboard.press("Enter")
    pagina.keyboard.press("Control+V")
    pagina.keyboard.press("Enter")
    pagina.wait_for_timeout(3000)
    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Enter")

    pagina.wait_for_timeout(12000)
