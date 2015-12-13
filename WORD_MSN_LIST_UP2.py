
from bs4 import BeautifulSoup
import requests


url = 'http://wordyn.blogspot.com'

html_source = requests.get(url)

html_txt = str(html_source.text)

soup = BeautifulSoup(html_txt, "html.parser")

linkList = []
for link in soup.find_all('a'):
    # print(link.get('href'))
    if link.get('href') != None:
        linkList.append(link.get('href'))



print (linkList)

msn_ContainingList = []

for item in linkList:
    if ".msn." in item:
        print (item)
        msn_ContainingList.append(item)

print(msn_ContainingList)
print(len(msn_ContainingList))

# print(soup.text)

'''
print(linkList)

for i in linkList:
    if i != None:
        if i.contains("msn"):
            print (i)
'''