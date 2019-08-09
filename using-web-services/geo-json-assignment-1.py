import json
import urllib.parse
import urllib.request

api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

query_parameters = dict()
query_parameters['address'] = address
query_parameters['key'] = api_key
url = service_url + urllib.parse.urlencode(query_parameters)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

results = js["results"][0]
print("Place id", results["place_id"])
