import urllib.request
import xml.etree.ElementTree as ET

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
# url = 'http://py4e-data.dr-chuck.net/comments_271732.xml'
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

total = 0
count = 0
results = tree.findall('comments/comment')
for item in results:
    count += 1
    total += int(item.find('count').text)

print("Count:", count)
print("Sum:", total)

