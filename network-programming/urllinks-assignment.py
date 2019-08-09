import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def get_links(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    current_position = 1
    new_url = ''

    for tag in tags:
        if current_position == position:
            new_url = str(tag.get('href', None))
            break
        current_position += 1

    return new_url


url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags
print('Retrieving: ' + url)
tags = soup('a')

index = 1
while index <= count:
    url = get_links(url, position)
    print('Retrieving: ' + url)
    index += 1
