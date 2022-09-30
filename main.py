import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  # headless - não demonstra o que realiza.
    pagina = navegador.new_page()
    pagina.goto("https://translate.google.com/")
    pagina.wait_for_timeout(1000)
    pagina.fill('xpath=//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]'
                '/div[3]/c-wiz[1]/span/span/div/textarea', 'Olá colegas, bom dia!')
    pagina.keyboard.press("Enter")

    pagina.wait_for_timeout(3000)
    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Enter")

    pagina.wait_for_timeout(4000)


'''

   pagina.click('xpath=//*[@id="ow87"]/div/span/button/div[3]')
   pagina.hover('xpath=//*[@id="ow87"]/div/span/button/div[3]')


    navegador = p.chromium.launch(headless=False) #headless - não demonstra o que realiza.
    pagina = navegador.new_page()
    pagina.goto("https://andersonmakiyama.com/fala-texto-em-portugues-ilimitado-e-gratis/")
    pagina.wait_for_timeout(2000)
    pagina.fill('xpath=//*[@id="texto"]', 'Ola jordan bom dia!')

    pagina.wait_for_timeout(1000)
    pagina.click('xpath=//*[@id="rate"]')
    pagina.keyboard.press("ArrowDown")
    pagina.keyboard.press("ArrowDown")
    pagina.keyboard.press("Enter")

    pagina.locator('xpath=//*[@id="post-175"]/div/div[2]/input[1]').click()

    pagina.wait_for_timeout(4000)
'''
''' 
    pagina.locator('xpath=//*[@id="post-175"]/div/div[2]/input[1]').click()
    pagina.click('xpath=//*[@id="post-175"]/div/div[2]/input[1]')

    pagina.wait_for_timeout(3000)
    pagina.keyboard.press("Enter")
    await pagina.click('BUTTON[type="button"]')

    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Enter")



'''
