from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

total = 0

tags = soup('span')
for tag in tags:
    total += int(tag.contents[0])

print(total)
