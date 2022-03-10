# "python3 packages.py" pour lancer ds terminal
import requests
# from requests import get    si on veux qu'une fonction du package

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
# Voir le code html source
print(page.content)