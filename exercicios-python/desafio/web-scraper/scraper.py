# O 'requests' serve pra viajar até a URL e baixar a página. 
# O 'BeautifulSoup' serve pra organizar a bagunça do código HTML.
import requests
from bs4 import BeautifulSoup

# O site para a extração de titulos
url = 'https://www.bbc.com/portuguese'

#os sites bloqueiam "bots". Com isso aqui, o programa é identificado como navegador Chrome comum no Windows
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print(f"[*] Conectando ao servidor da BBC News...")
# Disparando a requisição pra baixar o site
resposta = requests.get(url, headers=headers)

# Trava de segurança: se o site estiver fora do ar ou bloquear o acesso(Erro 404, 403), o programa para aqui e me avisa.
resposta.raise_for_status()

# Começando a limpeza nos dados
print("[*] Lendo e estruturando o HTML da página...")
# Transforma o texto do HTML numa árvore que o Python consegue pesquisar
soup = BeautifulSoup(resposta.text, 'html.parser')

# procurando todas as tags <h2> e <h3> (onde costumam ficar os títulos). 
# O .get_text(strip=True) remove todo o código em volta e deixa só as palavras.
titulos = [tag.get_text(strip=True) for tag in soup.find_all(['h2', 'h3']) if tag.get_text(strip=True)]

# Nome do arquivo de texto que vai ser criado no meu computador
nome_arquivo = 'titulos_noticias.txt'

# O 'with open' abre o arquivo, escreve tudo e fecha sozinho. Não tem perigo de corromper.
# O 'w' significa Write (escrever/criar) e o utf-8 é pra não bugar os acentos do português (ç, ã, é).
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    # Faço um loop passando por todos os títulos encontrados e salvo linha por linha no bloquinho de notas
    for titulo in titulos:
        arquivo.write(f"- {titulo}\n")

# Avisando no terminal que deu tudo certo e quantos títulos foram copiados
print(f"\n{len(titulos)} títulos foram extraídos e salvos no arquivo '{nome_arquivo}'.")