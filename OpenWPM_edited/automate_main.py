import os
import shutil
import sys
import os.path
from os import path
import subprocess


folderNames = ["beautifyTools", "clos_comp/simple", "clos_comp/advanced", "draftlogic", "jfogs",
    "js_obfus", "obfus_io/default", "obfus_io/high", "obfus_io/low", "obfus_io/medium", "original"]


# os.mkdir("/Users/rayngan/openWPM_data/clos_comp")
# os.mkdir("/Users/rayngan/openWPM_data/obfus_io")

restart = False

if restart:
    for folders in folderNames:
        sqlDir = "/home/c2/Documents/rayngan/Scripts-Replacing-Crawler/openWPM_data/" + folders
        shutil.rmtree(sqlDir)
        if(os.path.isdir(sqlDir)):
            continue
        os.mkdir(sqlDir)
else:
    for folders in folderNames:
        sqlDir = "/home/c2/Documents/rayngan/Scripts-Replacing-Crawler/openWPM_data/"
        path = os.path.join(sqlDir, folders)
        if(os.path.isdir(path)):
            continue
        os.mkdir(path)

done = False
run = True
if run:
    for i in range(848,849):
        scriptIndex = i + 1
        
        f = open(os.path.join(os.getcwd(), "counter.txt"), "w")
        f.write(str(scriptIndex))
        mitm_8080 = subprocess.Popen('mitmdump -s "./replaceAllScripts/replaceAllScripts_1.py" --listen-port 8080', close_fds=True, shell=True)
        openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8080" + " " + folderNames[0]
        openWPM_8080 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)
 
     
        # mitm_8081 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_2.py  --listen-port 8081', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8081" + " " + folderNames[1]
        # openWPM_8081 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8082 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_3.py  --listen-port 8082', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8082" + " " + folderNames[2]
        # openWPM_8082 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)
        
        
        # mitm_8083 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_4.py  --listen-port 8083', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8083" + " " + folderNames[3]
        # openWPM_8083 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8084 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_5.py  --listen-port 8084', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8084" + " " + folderNames[4]
        # openWPM_8084 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8085 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_6.py  --listen-port 8085', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8085" + " " + folderNames[5]
        # openWPM_8085 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8086 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_7.py  --listen-port 8086', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8086" + " " + folderNames[6]
        # openWPM_8086 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8087 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_8.py  --listen-port 8087', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8087" + " " + folderNames[7]
        # openWPM_8087 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)
        
        
        # mitm_8088 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_9.py  --listen-port 8088', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8088" + " " + folderNames[8]
        # openWPM_8088 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8089 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_10.py  --listen-port 8089', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8089" + " " + folderNames[9]
        # openWPM_8089 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        
        # mitm_8090 = subprocess.Popen('mitmdump -s ./replaceAllScripts/replaceAllScripts_11.py  --listen-port 8090', close_fds=True, shell=True)
        # openWPMCommand = "python2 /home/c2/Documents/rayngan/Scripts-Replacing-Crawler/OpenWPM_edited/demo.py" + " " + str(scriptIndex) + " " + "8090" + " " + folderNames[10]
        # openWPM_8090 = subprocess.Popen(openWPMCommand, close_fds=True, shell=True)

        # try:
        #     openWPM_8080.wait(100)
        #     mitm_8080.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8080.terminate()
        #     mitm_8080.terminate()
        # try:
        #     openWPM_8081.wait(100)
        #     mitm_8081.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8081.terminate()
        #     mitm_8081.terminate()
        # try:
        #     openWPM_8082.wait(100)
        #     mitm_8082.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8082.terminate()
        #     mitm_8082.terminate()
        # try:
        #     openWPM_8083.wait(100)
        #     mitm_8083.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8083.terminate()
        #     mitm_8083.terminate()
        # try:
        #     openWPM_8084.wait(100)
        #     mitm_8084.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8084.terminate()
        #     mitm_8084.terminate()
        # try:
        #     openWPM_8085.wait(100)
        #     mitm_8085.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8085.terminate()
        #     mitm_8085.terminate()
        # try:
        #     openWPM_8086.wait(100)
        #     mitm_8086.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8086.terminate()
        #     mitm_8086.terminate()

        # try:
        #     openWPM_8087.wait(100)
        #     mitm_8087.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8087.terminate()
        #     mitm_8087.terminate()

        # try:
        #     openWPM_8088.wait(100)
        #     mitm_8088.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8088.terminate()
        #     mitm_8088.terminate()

        # try:
        #     openWPM_8089.wait(100)
        #     mitm_8089.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8089.terminate()
        #     mitm_8089.terminate()

        # try:
        #     openWPM_8090.wait(100)
        #     mitm_8090.terminate()
        # except:
        #     print("Timeout Expired")
        #     openWPM_8090.terminate()
        #     mitm_8090.terminate()

      
          
   

    
   
 
