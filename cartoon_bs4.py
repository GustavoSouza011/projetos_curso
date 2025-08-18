import requests
from bs4 import BeautifulSoup

url = "https://www.cartoonnetwork.ca/"

# Faz a requisição para o site
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria o objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra a tag h1
    h1_tag = soup.find('h1')
    
    if h1_tag:
        print("Conteúdo da tag <h1>:", h1_tag.text.strip(), "faliu e hoje não tem desenho bão")
    else:
        print("Nenhuma tag <h1> encontrada.")
else:
    print(f"Erro ao acessar o site: {response.status_code}")
