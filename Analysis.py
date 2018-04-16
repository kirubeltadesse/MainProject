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
				if key == 'Waterfall view':
					pattern = r'[0-9][0-9]'
					if re.search(pattern, value):
						x = re.findall(pattern,value)
						rep = re.compile(r'\s+')
						time = re.sub(rep,'',str(x[:3]).replace("'",""))
						
						value = time.replace('18','2018').replace('[', '').replace(']','').replace(',','-')
						key = 'date'
					count_num_data += 1 

			
			data[catagory].setdefault(key,[]).append(value)
			
		cleaned_dict =  dict(data)
		for web in cleaned_dict.keys():
			#replace empty value with np.nan
			del cleaned_dict[web]['Waterfall view']
			del cleaned_dict[web]['web address']
			for x in cleaned_dict[web].keys():
				if '' in cleaned_dict[web][x]:
					for y in cleaned_dict[web][x]:
						cleaned_dict[web][x] = np.nan
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
#test.clean_up('test_result.txt')

'''
df2 = pd.DataFrame.from_dict({(i,j):value[i][j]
							for i in value.keys()
							for j in value[i].keys()},
							orient = 'index')
'''

df = pd.DataFrame(data=value)
dfT = df.transpose()

# conver to frame
df_2 =pd.DataFrame(data=dfT[u'Speed Index']).dropna()
s = df_2.apply(lambda x: pd.Series(x[u'Speed Index']), axis = 1).transpose().max()
print s

#print df[:1].describe()
#df_replace = dfT[:5][u'Speed Index']
#print dfT.describe()
#print dfT[:][u'Speed Index'].mean()             






