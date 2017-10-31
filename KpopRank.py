#Kpop Rank
import requests
from bs4 import BeautifulSoup

url = 'https://www.letras.mus.br/mais-acessadas/k-popk-rock/'
r = requests.get(url)

nome = BeautifulSoup(r.content, "html.parser")

musica = nome.findAll("b")

for i in musica:
    print(i.getText())











