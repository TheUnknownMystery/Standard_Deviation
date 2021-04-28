# Imported Libaries
# math,pandas,plotly_express
import csv
import math
import pandas as pd
import plotly_express as px

# File variable for storing the file object
File_Object = open('Data.csv', newline='')
reader = csv.reader(File_Object)

List_1 = list(reader)
List_1.pop(0)

Height_List = []


for i in range(len(List_1)):
    Numbers = List_1[i][1]
    Height_List.append(float(Numbers))


l = len(Height_List)
Total = 0

for x in Height_List:
    Total += (x)

mean = Total/l

# print(mean)
SquaredList = []

for val in Height_List:
    a = int(val) - mean
    a = a**2

    SquaredList.append(a)

sum1 = 0

for i in SquaredList:
    sum1 = sum1 + 1

result = sum1 / (len(Height_List)-1)
std_Deviation = math.sqrt(result)

print(std_Deviation)


# Graph parth
Csv_File = pd.read_csv('Data.csv')
Graph = px.scatter(Csv_File, x='index', y='Data', color='index')

Graph.update_layout(shapes=[

    dict(
 
    type = 'line',
    y0   = mean,
    y1   =  mean,
    x0 = 0,
    x1 = Total

    )
])
Graph.show()
