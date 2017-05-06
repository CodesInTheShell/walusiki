#################################
#        CodesInTheShell.........
#
#################################

import requests

# url varies depending on your target
url = 'http://192.168.142.128/mutillidae/'
#adding header for the request to became a bit anonymous
head = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

#Printing a simple banner
print("""
#############################################
# This program is a part of walusiki project.
# Feel free to use and modify the code.
#
#                 by: CITS
#############################################
""")
print("Program running...")
print("Performing resource discovery on " + url + "\n")

#We will use a wordlist from fuzzdb
for word in open('raft-small-files.txt', 'r').readlines():

    try:
        #append each word to the url
        fuzz_url = url + word

        #http://192.168.142.128/mutillidae/word where word are words from raf-small.files.txt
        #e.i http://192.168.142.128/mutillidae/.htpasswds that will return 403 Forbidden
        r = requests.get(fuzz_url, headers=head)

        #We any response code from server but not 404 Not Found
        if r.status_code != 404:
            #We would like to know the url that returns something
            print(str(r.status_code) + ' status of url ' + fuzz_url)

    except Exception as e:
        print(e)