# Site Scraper Automatizado com Selenium
## Sobre
Este script utiliza a biblioteca Selenium para automatizar a abertura de vários sites e realizar pesquisas em cada um deles, de acordo com o termo inserido pelo usuário. A pesquisa é personalizada para cada site, substituindo automaticamente o termo de pesquisa em uma URL específica. O objetivo inicial era de facilitar a busca de componentes eletrônicos em várias lojas online simultaneamente, mas pode ser facilmente extendido para atender qualquer produto.

## Requisitos

- Selenium - Biblioteca utiliada para automações Web

    Instale o Selenium executando o comando abaixo:
    ```
    pip install selenium
    ```

- ChromeDriver - Uma ponte entre o Google Chome e Scripts Python
    
    Faça o download do [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads/version-selection?hl=pt-br) compatível com a sua versão do Google Chrome.

    Coloque o arquivo chromedriver.exe no mesmo diretório do script. 

## Funcionamento

Ao executar o arquivo main.py irá abrir todos os sites configurados no arquivo lista_site.py e aguardar o termo de pesquisa. Simples assim, ao digitar o item desejado o scrit ira pesquisar por esse termo em todos os sites. 

## Estrutura do Dicionário de Sites 
Abaixo está o exemplo de como os sites são adicionados ao dicionário no arquivo lista_site.py:

```python
    site_dict = {
    0: {
        "nome": "Amazon",
        "url": "https://www.amazon.com.br",
        "pesquisar": True,  # Se True, o site será incluído nas pesquisas
        "url_pesquisa": "https://www.amazon.com.br/s?k=#",# URL de pesquisa com "#" representando o termo a ser substituído
    },
    1: {
        "nome": "Mercado Livre",
        "url": "https://www.mercadolivre.com.br/",
        "pesquisar": True, 
        "url_pesquisa": "https://lista.mercadolivre.com.br/#", 
    },
    }
    # Outros sites...
```

## Parâmetros
- **nome**: Nome do site.
- **url**: URL principal do site.
- **pesquisar**: Se True, o site será incluído na pesquisa.
- **url_pesquisa**: URL de pesquisa, onde o caractere # será substituído pelo termo de pesquisa inserido.



## Exemplo de utilização
Esse script foi criado para facilitar a vida na hora de pesquisar vários itens de eletrônica e montar uma lista para orçamento. Antes, eu tinha que ficar pesquisando manualmente o mesmo componente em vários sites até achar o melhor preço, o que era bem trabalhoso. Agora, com o script, ele faz essa busca automaticamente em diversos sites, como você pode ver no vídeo abaixo.

<iframe width="560" height="315" src="https://youtu.be/RUkYuMXMgZQ" frameborder="0" allowfullscreen></iframe>
