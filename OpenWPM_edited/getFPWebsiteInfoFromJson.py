import json
import os
import os.path
from os import path

def website_url(index):
    print(index)
    sites = set()

    jsonLocation = "/Users/rayngan/Desktop/FPResearch/fp-obfuscation/scripts/obfuscated/new_fingerprinting_domains.json"
    f = open(jsonLocation, "r")

    data = json.loads(f.read())

    # if not path.exists(os.path.join(os.getcwd(), "counter.txt")):
    #     f = open(os.path.join(os.getcwd(), "counter.txt"), "w")
    #     f.close()


    for theHash, urls in data.items():
        topURL = str(urls[1])
        if not topURL in sites:
            sites.add(topURL)
            flag = True

        # print(len(sites))
        if len(sites) == index:
            # first item is the top url, second item is the hash
            allInfo = []
            allInfo.append(topURL)
            allInfo.append(theHash)

            target = open(os.path.join(os.getcwd(), "allCrawl.txt"), "a")
            target.write(str(topURL) + "\n")
            target.close()

            f.close()
            return allInfo

    f.close()
    return None
