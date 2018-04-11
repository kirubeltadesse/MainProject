import pandas as pd
import numpy as np
import re
import collections

class analysis():
	def __init__(self, num_data):
		self.num_data = num_data

	# clean up a row data 
	def clean_up(self, file_name): 
		with open(file_name) as infile:
			contents = infile.read()
			data = contents.replace('%20', ' ')
			data = data.replace('%2F%2F','://')
			info = data.replace(';','\n')
			info = info.replace('%3D%3D%3D%3D','\n')
			info1 = info.replace('%3A','')
			# f = open("data.txt","a+")
			# f.write(info1 +"\n")
			# f.close()

			self.prepare(info1)
	
	# change to list with in a dictionary 
	def prepare(self, file_name, from_file=False):
		collection = []
		data= collections.defaultdict(dict) 
		count_num_data = 0

		if from_file:
			with open(file_name,'r') as l_file:	
				content = l_file.read()
		else:
			content = file_name

		# convert the data into one hot list
		line = content.split('\n')

		for each in line:

			values = each.split(':')
			# print values, len(values)

			if len(values) == 3:

				key, value_1, value_2 = values
				value = value_1+":"+ value_2

				if key == 'web address':
					catagory = value

			elif len(values) == 2:
				key, value = values
			
			else:                   
			#	if count_num_data %100 == 0:
			#	print key, value, len(value)
				pass

				'''
				# add time variable
				'''
				if key == 'Waterfall view':
					pattern = r'[0-9][0-9]'
					if re.search(pattern, value):
						x = re.findall(pattern,value)
						rep = re.compile(r'\s+')
						time = re.sub(rep,'',str(x[:3]).replace("'",""))
						
						value = time.replace('18','2018').replace('[', '').replace(']','').replace(',','-')
						key = 'date'
					count_num_data += 1 

			'''
			if value == '':
				print "True"
			'''
			
			data[catagory].setdefault(key,[]).append(value)
			
		cleaned_dict =  dict(data)
		for web in cleaned_dict.keys():
			del cleaned_dict[web]['Waterfall view']
			del cleaned_dict[web]['web address']

			if cleaned_dict[web].has_key(''):
				del cleaned_dict[web]['']
			else:
				pass
		
		print "The number of data collected is: ", count_num_data
		return cleaned_dict


	# produce tabel, chart, and graph
	def plot(self, dataframe):
		return dataframe.plot()
	
	def prop(self, dataframe):
		return dataframe.columns
	
		
test = analysis(1)
value =  test.prepare('data.csv', True)
test.clean_up('test_result.txt')

df = pd.DataFrame(data=value)
#print df.columns
print df.head(5)

#print df.columns([u'date', u'web address'])
# print df.set_index('date')
#print df.sort([u'date', u'web address', u'(Doc complete) Byets in', u'(Doc complete) Requests', u'(Fully loaded) Bytes in', u'(Fully loaded) Requests', u'(Fully loaded) Time', u'DOM elements', u'First byte', u'Load time', u'Speed Index', u'Start render'])
#print df.index([u'web address'])

# Index([u'', u'(Doc complete) Byets in', u'(Doc complete) Requests', u'(Fully loaded) Bytes in', u'(Fully loaded) Requests', u'(Fully loaded) Time', u'DOM elements', u'First byte', u'Load time', u'Speed Index', u'Start render', u'Waterfall view', u'date',u'web address', u'web addresshttp'], dtype='object')

