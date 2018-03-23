import pandas as pd
from urlparse import urlparse
import urllib2
import urllib
import re


try:
	url = urllib2.urlopen('https://searchenginesmarketer.com/company/resources/university-college-list/')
	headers = {}
 
	headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)   AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	req = urllib2.Request(url, headers=headers)
	respData = resp.read()
	df = pd.read_html(respData)
except Exception as e:
	print str(e)
#Eprint df
