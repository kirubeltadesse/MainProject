import pandas as pd
import numpy as np

class analysis():
	def __init__(self, num_data):
		self.num_data = num_data

	def clean_up(self, file_name): 
		with open('test_result.txt') as infile:
			contents = infile.read()
			data = contents.replace('%20', ' ')
			data = data.replace('%2F%2F','://')
			info = data.replace(';','\n')
			info = info.replace('%3D%3D%3D%3D','\n')
			info1 = info.replace('%3A','')
		return info1

	def plot(self, dataframe):
		return dataframe.plot()
		
	def prepare(self, file_name):
		collection = []
		data= {} 
		with open(file_name,'r') as l_file:	
			content = l_file.read()

			# convert the data into one hot list
			line = content.split('\n')

			for each in line:
				#print each
				values = each.split(':')

				if len(values) == 3:
					key, value_1, value_2 = values
					value = value_1+":"+ value_2
				elif len(values) == 2:
					key, value = values
				else:
					pass
				data[key] = value
				collection.append(data)
		return collection


test = analysis(1)

value =  test.prepare('data.csv')
df = pd.DataFrame(data=value)
print df.head()
