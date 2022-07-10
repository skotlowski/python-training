import random
import requests
from bs4 import BeautifulSoup

url ='https://stat.gov.pl/badania-statystyczne/sprawozdawczosc/intrastat/alfabetyczny-wykaz-krajow/'

response = requests.get(url)

#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all(attrs={"style": "margin-left: 40px;"})

panstwa = [item.text for item in data]

print(f'Podaj stolice kraju: {random.choice(panstwa)}')


