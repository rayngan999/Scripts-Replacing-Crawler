from __future__ import absolute_import
from six.moves import range
from automation import CommandSequence, TaskManager

import time
import getFPWebsiteInfoFromJson
import subprocess
import sys
import os
import shutil

# The list of sites that we wish to crawl
NUM_BROWSERS = 1


siteIndex = int(sys.argv[1])
portNumber = int(sys.argv[2])
obfuscator = str(sys.argv[3])

sqlDir = "/home/c2/Documents/rayngan/Scripts-Replacing-Crawler/openWPM_data/" + obfuscator + "/sqlite"
logDir = "/home/c2/Documents/rayngan/Scripts-Replacing-Crawler/openWPM_data/" + obfuscator +"/log"
allSqlDir = "/home/c2/Documents/rayngan/Scripts-Replacing-Crawler/openWPM_data/" + obfuscator +"/all_sqlite"

print("Siteindex is: " + str(siteIndex))
print("Obfuscator is: " + obfuscator)
print("Port number is: " + str(portNumber))
sites = getFPWebsiteInfoFromJson.website_url(siteIndex)
print ("Site is: " + str(sites))


# Loads the manager preference and 3 copies of the default browser dictionaries
manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)

# Update browser configuration (use this for per-browser settings)
for i in range(NUM_BROWSERS):
    # Enable flash for all three browsers
    browser_params[i]['disable_flash'] = False
    browser_params[i]['cookie_instrument'] = True
    browser_params[i]['js_instrument'] = True
    browser_params[i]['save_javascript'] = True
    browser_params[i]['http_instrument'] = True
    browser_params[i]['headless'] = False
    browser_params[i]['save_documents'] = True
    browser_params[i]['caching_disabled'] = True
    
    

# Update TaskManager configuration (use this for crawl-wide settings)
if not os.path.isdir(sqlDir):
    os.mkdir(sqlDir)

manager_params['data_directory'] = sqlDir

if not os.path.isdir(logDir):
    os.mkdir(logDir)

manager_params['log_directory'] = logDir

# Instantiates the measurement platform
# Commands time out by default after 60 seconds
manager = TaskManager.TaskManager(manager_params, browser_params, portNumber)

# Visits the sites with all browsers simultaneously
site = sites[0]
command_sequence = CommandSequence.CommandSequence(site, reset=True)

# Start by visiting the page
command_sequence.get(sleep=5, timeout=30)
command_sequence.scroll_page()
command_sequence.recursive_dump_page_source()

# dump_profile_cookies/dump_flash_cookies closes the current tab.
command_sequence.dump_profile_cookies()
# index='**' synchronizes visits between the three browsers
manager.execute_command_sequence(command_sequence)

# Shuts down the browsers and waits for the data to finish logging
manager.close()

# do the clean up
oldFileName = "crawl-data.sqlite"
newFileName = sites[1] +".sqlite"
newPath = "/home/c2/Documents/rayngan/Scripts-Replacing-Crawler/openWPM_data/" + obfuscator + "/all_sqlite"
oldSql = os.path.join(sqlDir,oldFileName)
newoSql = os.path.join(newPath,newFileName)

# move the sql file together
if os.path.exists(oldSql):
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    os.rename(os.path.join(sqlDir,oldFileName), os.path.join(newPath,newFileName))

# delete both log directory and sql directory
if os.path.exists(sqlDir):
    shutil.rmtree(sqlDir)

if os.path.exists(logDir):
    shutil.rmtree(logDir)
