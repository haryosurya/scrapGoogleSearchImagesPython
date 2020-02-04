import requests
from bs4 import BeautifulSoup

def findUrl(tag):
	i,j = tag['href'].find('?q='),tag['href'].find('&')
	return tag['href'][i+3:j]

searchItem = input()
basePath = 'https://www.google.com/'
normUrl = basePath + 'search?q=' + searchItem
imgUrl = basePath + 'search?q=' + searchItem + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjKho3VyvvjAhWE7HMBHe7RAggQ_AUIEygD'

resNorm = requests.get(normUrl)
resImg  = requests.get(imgUrl )




with open('i.html','w') as f:
	f.write(resImg.text)



soup = BeautifulSoup(resImg.text,'html.parser')
imgAncs = soup.find_all('a')
imgAncs = [findUrl(a) for a in imgAncs if a['href'][0:4] == '/url' ]

try:
	imgThbs = [i['src'] for i in soup.find_all('img')  if 'src' in i.attrs and 'http://t0.gstatic.com/images' in i['src'] ]
except:
	pass

l = len(imgAncs) if len(imgAncs)<len(imgThbs) else len(imgThbs)

with open('search.html','w') as fs:
	for i in range(l):
		fs.write('<a href={} target=_blank><img src={}></a><br><br><br>'.format(imgAncs[i][0],imgThbs[i]))




