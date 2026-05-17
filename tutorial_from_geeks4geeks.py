import requests
from bs4 import BeautifulSoup

# requrst to the ULR
r = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')

# parsing HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# printing details from the HTML
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)