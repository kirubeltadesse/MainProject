#import urllib.request
from urlparse import urlparse
import urllib2
import urllib
import re


#x = urllib2.urlopen('http://www.webpagetest.org/')
#print(x.read())
url = 'http://pythonprogramming.net'
#values = {'s':'basic',
#		  'submit':'search'}

values = 'www.p3strategies.net'

data = urllib.urlencode(values)
data = data.encode('utf-8')
print data
#req = urllib2.Request(url,data)
#resp = urllib2.urlopen(req)
#respData = resp.read()
#
##print respData
#
#paragraph = re.findall(r'<p>(.*?)</p>', respData) #. any charactor
#
#
#for eachP in paragraph:
#	print eachP
'''
try:
	x = urllib2.urlopen('https://www.google.com/search?q=test')

	print x.read()

except Exception as e:
	print str(e)

try:
	url = 'https://www.google.com/search?q=test'
	headers = {}
	headers['User-Agent'] ='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	req = urllib2.Request(url, headers=headers)
	resp = urllib2.urlopen(req)
	respData = resp.read()

	saveFile = open('withhead.txt', 'w')
	saveFile.write(str(respData))
	saveFile.close()
except Exception as e:
	print(str(e))

'''







