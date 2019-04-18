#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*_



import requests
host = "http://test.pipifit.com/shelf"
url1 ="/press/history"
url=host+url1
header = {"token":"f19a518b0724032bb09c4b10c464d5eb6cf73983e147214105705ebee79777c2"}


req=requests.get(url=url,headers=header)

print(req.text)
