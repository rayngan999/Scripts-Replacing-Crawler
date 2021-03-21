import json

def website_url(input_count):
    sites = set()
    hashes = []
    f = open('fingerprinting_domains.json', "r")

    data = json.loads(f.read())

    for hash in data:
        flag = False
        for i in data[hash]:
            if not i['top_url'] in sites:
                sites.add(i['top_url'])
                flag = True
                break
        if flag == True:
            hashes.append(hash)
        if len(hashes) == input_count:
            break

    return sites

def getHash(input_count):
    hashes = []
    f = open('fingerprinting_domains.json', "r")

    data = json.loads(f.read())

    for i in data:
        hashes.append(i)
        if len(hashes) == input_count:
            break


    return hashes