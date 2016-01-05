import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
parser = "html5lib"
soup = BeautifulSoup(html, parser)

tags = soup('p')
print len(tags)
