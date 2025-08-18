import requests
from bs4 import BeautifulSoup

# URL da página
url = "https://sp.senai.br/unidade/santanadeparnaiba/"

# Requisição HTTP
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parse do conteúdo HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar a primeira tag <h1>
    h1_tag = soup.find("h1")

    if h1_tag:
        print("Conteúdo da tag <h1>:")
        print(h1_tag.get_text(strip=True), "o melhor do Brasil")  
    else:
        print("Tag <h1> não encontrada.")
else:
    print(f"Erro ao acessar o site. Status code: {response.status_code}")
