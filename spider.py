#################################
#        CodesInTheShell.........
#
#################################

import requests
from bs4 import BeautifulSoup

print("Program running...")
# ulr varies depending on your target
url = 'http://192.168.142.128/mutillidae/'
#header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

links_list = []
crawled_links = []

#Browse the target website
r = requests.get(url)

#Parse the response
soup = BeautifulSoup(r.content,"html.parser")

#Find all links on the response page
links = soup.find_all("a")

#Filtering the links on the target domain only
for link in links:
    if './' in link.get("href") and len(links_list) < 100:
        links_list.append(link.get("href"))
        crawled_links.append(link.get("href"))

#Crawling the links for the first response for other links and add them to the crawled links
for l in links_list:
    new_link = url + l[2:]
    new_r = requests.get(new_link)
    new_soup = BeautifulSoup(new_r.content, "html.parser")
    links_per_page = new_soup.find_all("a")

    for li in links_per_page:
        try: #Some produce errors
            if './' in li.get("href") and li not in crawled_links:
                crawled_links.append(li.get("href"))
        except TypeError:
            pass

#Removing duplicated links
sorted_crawled_links = set(crawled_links)
print("\n")
print("There are " + str(len(sorted_crawled_links)) + " links on " + url + " domain.")
print("\n")
print("\n")
print("Here are the pages: \n")

#Printing
for c in sorted_crawled_links:
    print(c)

