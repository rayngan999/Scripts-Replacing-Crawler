from mitmproxy import http
import json
# import requests
import os
import sys
import os.path
from os import path

# 11 folders
folderNames = ["beautifyTools","clos_comp/simple","clos_comp/advanced","draftlogic","jfogs","js_obfus","obfus_io/default","obfus_io/high","obfus_io/low","obfus_io/medium","original"]
JsonDir = "/Users/rayngan/Desktop/FPResearch/fp-obfuscation/scripts/obfuscated"
JsonFileName = "new_fingerprinting_domains.json"
ScriptsDir = "/Users/rayngan/Desktop/FPResearch/fp-obfuscation/scripts/obfuscated"
JsonPath = os.path.join(JsonDir, JsonFileName)
# a dictionary used for detecting the script url, also finding corresponding file by hash
scriptURLToHash = {}

obfIndex = siteIndex = 7
# start with only a small part
def initialize_dict():
    with open(JsonPath) as f:
        data = json.load(f)
        count = 0

        for theHash, urls in data.items():
            scriptURL = str(urls[0])
            hashString = str(theHash)
            scriptURLToHash[scriptURL] = hashString

   



initialize_dict()

ScriptName = folderNames[int(obfIndex) - 1]
ScriptsPath = os.path.join(ScriptsDir, ScriptName)


def response(flow):
    if flow.request.pretty_url in scriptURLToHash:
        ScriptName = folderNames[int(obfIndex) - 1]
        ScriptsPath = os.path.join(ScriptsDir, ScriptName)
        # current script's url
        script = flow.request.pretty_url
        # get the original hash from url
        myHash = scriptURLToHash[script]
        hashPath = os.path.join(ScriptsPath, myHash)
        hashPath = hashPath + ".js"

        if path.isfile(hashPath):
            with open(hashPath) as f:
                s = f.read()
                flow.response.text=s
                idDoc = open(os.path.join(os.getcwd(), "./urlToVisitID/urlsToVisitID_obfus_io_default.txt"), "a")
                idDoc.write("Index:" + str(obfIndex) + " script:" + script + " hash:" + myHash + "\n")
