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
import re
import collections
import pandas as pd


with open('words2.json') as infile:
	contents = infile.read()
	data = contents.replace('%20', ' ')
	info = data.replace(';','\n')
	info1 = info.replace('%3A','')
	print info1
'''
	contents = infile.read()
	for x in range(100):
		data = contents.split('%20')
		print data
'''


