import requests

"""headers= requests.util.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/2010001 Firefox/52.0'})"""

from bs4 import BeautifulSoup

ur= "https://en.wikipedia.org/wiki/"
film=input("Enter the film : ")
url=ur+film
req= requests.get(url)
soup=BeautifulSoup(req.content,'html.parser')

plot=[]
tag=soup.select_one('#Plot').find_parent('h2').find_next_sibling()
while tag.name=='p':
    plot.append(tag.text.rstrip())
    tag=tag.find_next_sibling()

st=" "
for i in plot:
    st+=i
    st+="\n\n"

print(st)




