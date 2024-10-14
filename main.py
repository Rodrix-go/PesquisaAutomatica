#Importanto bibliotecas - pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lista_site import site_dict

service = Service(r'chromedriver.exe')
options = webdriver.ChromeOptions()

options.page_load_strategy = 'none'

navegador = webdriver.Chrome(service=service, options=options) 
navegador.maximize_window()


#Abrir todas os sites
for id, site_info in site_dict.items():
    if site_info["pesquisar"]: # Verifica se precisa pesquisar
        print("Abrindo site:", site_info["nome"])
        navegador.switch_to.new_window('tab') # Abre uma nova janela
        site_info["window_handle"] = navegador.current_window_handle # Adiciona o handle dessa janela             
        navegador.get(site_info['url']) # Realia a pesquisa do site


#Realiza as pesquisas
while True:
    
    item_pesquisar = input("Digite o que deseja pesquisar: ")

    for site_id, site_info in site_dict.items():

        if site_info["pesquisar"]:
            navegador.switch_to.window(site_info["window_handle"])  
            item_pesquisar =  item_pesquisar.replace(" ", "%20") # Substitui o caracter espaço pelo seu valor em ASCII
            url_pesquisa = site_info["url_pesquisa"]
            url_pesquisa = url_pesquisa.replace("#", item_pesquisar) # Substitui a # pelo nome do item tratado
            navegador.get(url_pesquisa) # Realiza a pesquisa


            