import requests 
from bs4 import BeautifulSoup

s = requests.Session()

url_base = "https://lista.mercadolivre.com.br/"

produto_nome = input('Qual o produto para busca? ')

conteudo = s.get(url_base + produto_nome) #passando o produto como parâmetro de busca

site = BeautifulSoup(conteudo.text, 'html.parser') #pegando o conteúdo extraído e deixando bonitinho no formato html

#lista com todos os produtos resultado da busca
produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core ui-search-result--advertisement andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    #valor R$
    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    print(produto.prettify())
    print('Título do produto:', titulo.text)
    print('Link do produto:', link['href'])

    if (centavos):
        print('Preço do produto: R$', real.text + ',' + centavos.text)
    else:
        print('Preço do produto: R$', real.text)
    
    print('\n\n')
    break