import urllib.request
import json

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url = 'http://py4e-data.dr-chuck.net/comments_271733.json'

url = input("Enter location: ")
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

total = 0
count = 0
for item in js["comments"]:
    total += int(item["count"])
    count += 1

print("Count:", count)
print("Sum:", total)




