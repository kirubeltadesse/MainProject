################################################################################
# 			using the webpage.com API
#			To extract the data to the required metrix
#			
#			https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/scripting
#		https://css-tricks.com/use-webpagetest-api/ttps://sites.google.com/a/webpagetest.org/docs/using-webpagetest/scripting
	
#			Use yslow or 
################################################################################



########
# usefull tutorial on 
# https://www.youtube.com/watch?v=FmsLJHikRf8
# bin/phantomjs --help ***besically you can tell the browser what to do 
########
import urllib2
import json

webpage_api = 'A.57c0ecce925470118d73687951af28ee'
result/180316_5B_2a0dc3b30a18c3ed09cf48e701686b6f/
result/180316_MH_e01f18306efafe6a9fe8ba9e93a4dcbb/

try:
	url = 'http://www.webpagetest.org/'
	req  = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	respData = resp.read()

	saveFile = open("result.txt", 'w')
	saveFile.write(str(respData))
	saveFile.close()

	

except Exception as e:
	print str(e)


