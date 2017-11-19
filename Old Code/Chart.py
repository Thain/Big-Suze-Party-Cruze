import pygal
import pandas as pd
import cairosvg

df = pd.read_csv('/Users/raphaelletseng/Desktop/Transportation/NYC General Transport/NYC-vehicle-collisions.csv')

#create pie chart
pie_chart=pygal.Pie()
pie_chart.title = 'BOROUGH ACCIDENTS'

df = df['BOROUGH'].value_counts(1).reset_index()
df.columns = ['BOROUGH', 'COUNT']
#print (df)

names = df['BOROUGH']
#print(names)
percentages = df['COUNT']
#print(percentages)

for x in range(0, df.shape[0]):
   pie_chart.add(names[x], percentages[x])
   #print (x)

pie_chart.render_to_file('piechart5.svg')
svg = open(file='piechart5.svg')
cairosvg piechart5.svg -o piechart5.png
