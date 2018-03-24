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
import pandas as pd
import numpy as np


with open('words2.json') as infile:
	contents = infile.read()
	data = contents.replace('%20', ' ')
	data = data.replace('%2F%2F','://')
	info = data.replace(';','\n')
	info = info.replace('%3D%3D%3D%3D','\n')
	info1 = info.replace('%3A','')
	print info1

'''
	contents = infile.read()
	for x in range(100):
		data = contents.split('%20')
		print data
'''
'''
def univ_list():

	df = pd.read_excel('univ_college_websites.xlsx', sheet_name="Sheet1")
	df2 = df.set_index('School Name')
	mylist = np.array(df2['URL'])
	unvi_web = pd.DataFrame(data=mylist[:100])
	unvi_web.to_json('univ_college.json')

	#return unvi_web

univ_list()
'''
