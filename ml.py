import requests
import json
result=requests.get('https://disease.sh/v3/covid-19/all')
result.status_code
result.text
response = result.json()
response
from matplotlib import pyplot as plt 
import numpy as np

world = ['TOTALCASES', 'TODAYCASES','TOTALRECOVERED', 'TOTALDEATH']

data = [response.get('cases'), response.get('todayCases'), response.get('recovered'), response.get('deaths')]
colors = ['blue', 'purple', 'green', 'red']
myexplode = [0, 0.1, 0, 0]

fig = plt.figure(figsize =(5, 3)) 

plt.pie(data, labels = world, explode = myexplode,colors=colors, autopct='%1.1f%%', startangle=140)


plt.savefig("plot.png",dpi=300)
globe = plt.savefig("plot.png",dpi=300)

plt.show()