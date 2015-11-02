import urllib2
from bs4 import BeautifulSoup

url="https://www.nytimes.com"

request = urllib2.urlopen(url)
result = request.read()
#print result
#soup=BeautifulSoup(result,'html.parser')


print soup.find_all('a'):

