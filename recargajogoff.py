import requests
from bs4 import BeautifulSoup

# URL que você quer acessar
url = "https://hype.games/br/free-fire"

# Faz a requisição HTTP para pegar o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Cria o objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Procura a tag <h1>
    h1_tag = soup.find('h1')

    if h1_tag:
        print("Conteúdo da tag <h1>:", h1_tag.text.strip(), "é gorpe fdp !!")
    else:
        print("Tag <h1> não encontrada.")
else:
    print(f"Erro ao acessar a página: {response.status_code}")
