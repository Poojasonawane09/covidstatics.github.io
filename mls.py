import requests
import json
result=requests.get('https://api.rootnet.in/covid19-in/stats/latest')
result.status_code
result.text
response = result.json()
response
from matplotlib import pyplot as plt
import numpy as np



india = ['TOTALCASES', 'TOTALRECOVERED', 'TOTALDEATH']
colors = ['blue', 'green', 'red']

data = [response.get('data').get('summary').get('total'), response.get('data').get('summary').get('discharged'),response.get('data').get('summary').get('deaths')]
myexplode = [0, 0, 0.1]

fig = plt.figure(figsize =(5, 3))
plt.pie(data, labels = india, explode = myexplode,colors=colors, autopct='%1.1f%%', startangle=140)

plt.savefig('india.png',dpi=300) 
country = plt.savefig('india.png',dpi=300) 
         
 
plt.show()