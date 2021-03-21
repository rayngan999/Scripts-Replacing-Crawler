import json
import os

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
                target = open(os.path.join(os.getcwd(), "newIndexFileMapping.txt"), "a")
                target.write(str(len(sites)) + " top:" + i['top_url'] + " script:" + i['script_url'] + "\n")
                target.write(hash + "\n")
                flag = True
                break
        if flag == True:
            hashes.append(hash)
        if len(hashes) == input_count:
            break

    return sites

website_url(50)

def getHash(input_count):
    hashes = []
    f = open('fingerprinting_domains.json', "r")

    data = json.loads(f.read())

    for i in data:
        hashes.append(i)
        if len(hashes) == input_count:
            break


    return hashes