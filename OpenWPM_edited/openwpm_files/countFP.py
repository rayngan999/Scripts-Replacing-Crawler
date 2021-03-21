import sys
import getWebsite

def count(fileName):
    f = open(fileName, "r")

    hashes = set()
    lines = f.readlines()
    # print("Original Hash Count: " + str(len(lines)))
    # count = 0
    for i in lines:
        hashes.add(i)
        # print(i)

    # print("After Hash Count: " + str(len(hashes)))
    return hashes


myHashes = count(sys.argv[1])
originalHashes = getWebsite.getHash(50)

countMatchHash = 0
for hash in myHashes:
    if hash in originalHashes:
        countMatchHash = countMatchHash + 1

print("Total Match Hash: " + str(countMatchHash))
urls = getWebsite.website_url(50)

count = 0
for url in urls:
    print()
