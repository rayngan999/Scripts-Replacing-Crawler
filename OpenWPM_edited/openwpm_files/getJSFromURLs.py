import json
import requests
import os

hash_f = open('hashContent.txt', "r")
json_f = open('mapping_with_hash.json', "r")

allHash = set()
allJson = set()

lines = hash_f.readlines()
for line in lines:
    s = line.replace('\n', '')
    allHash.add(s)


count = 0
json_data = json.loads(json_f.read())
for data in json_data:
    if json_data[data]['content_hash'] in allHash and not json_data[data]['new_url_key'] in allJson:
        myHash = json_data[data]['content_hash']
        myURL = json_data[data]['new_url_key']
        allJson.add(myURL)
        allHash.remove(myHash)
        # print(json_data[data]['new_url_key'])
        if myHash == '':
            continue
        try:
            r = requests.get(myURL, allow_redirects=True)
            open('newJS/'+myHash+".js", 'wb').write(r.content)
            target = open(os.path.join(os.getcwd(), "jsHashToURL.txt"), "a")
            target.write(myHash + "  " + json_data[data]['new_url_key'] + "\n")
        except requests.exceptions.ConnectionError:
            continue


print(len(allJson))
print(len(allHash))
