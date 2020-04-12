# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:55:46 2020

@author: Dell
"""
import requests 
from bs4 import BeautifulSoup 

def toint(sales):
    sale=[]
    for item in sales:
        nd=''
        for i in item.split(','):
            nd=nd+i
        sale.append(int(nd))
    
    return(sale)
  
def incdec(l):
    count=0
    for i in range(1,len(l)):
        if(l[i-1]>l[i]):
            count+=1
    return("went down "+str(count)+"time in "+str(len(l))+" years ")
URL = "https://www.screener.in/company/SPICEJET/"
r = requests.get(URL) 

  
soup = BeautifulSoup(r.content, 'html.parser') 
table=soup.find(id='profit-loss') 
data_all=table.find_all(class_='responsive-holder')
#print(data_all)

# sales

dat=data_all[0].find_all(class_="stripe")
data=(dat[0].find_all('td'))[1:]
sales=[d.get_text() for d in data]
sales=toint(sales)
print("sales "+incdec(sales))
print("company sales increased by "+str(((sales[-1]-sales[0])/sales[0])*100)+"% in last "+str(len(sales))+"years")

#operating profits 

dat_op=data_all[0].find_all(class_="stripe strong")
data_op=(dat_op[0].find_all('td'))[1:]
ops=[d.get_text() for d in data_op]
ops=toint(ops)

# dividents pay %

dps=[]
dat_div=data_all[0].find_all(class_="")
for dd in dat_div:
    t=dd.find(class_='text')
    if(t):
        if(t.get_text().strip()=="Dividend Payout %"):
            data_div=(dd.find_all('td'))[1:]
            dps=[d.get_text() for d in data_div]
            dps=[int(d1[:-1]) for d1 in dps]
            break
c=0
for i in dps:
    if(i==0):
        c=c+1
if(c==0):
    print("company is giving a dividents pay every year")
else:
    print("company has not paid its divident for "+str(c)+" years")
        

# Net profit 

dat_net=data_all[0].find_all(class_="strong")
data_net=(dat_net[-1].find_all('td'))[1:]
net=[d.get_text() for d in data_net]
net=toint(net)
print("net profits "+incdec(net))
'''   
# years i.e head of table

dat_y=data_all[0].find("thead")
data_y=dat_y.find_all('th')
year=[int((d.get_text().split())[-1]) for d in data_y[1:]]
'''
# compound growth in sale 

rows=table.find(class_="row")
rows=rows.find_all(class_="three columns ranges-table")
com=rows[0].find_all('td')
comp=[c.get_text() for c in com]
comp=[comp[i] for i in range(1,len(comp),2)]
cmpg=[]
for i in comp:
    if(len(i)<2):
        cmpg.append(0)
        continue
    else:
        cmpg.append(float(i[:-1]))
if(cmpg[0]<=cmpg[1] and cmpg[1]<=cmpg[2]):
    print("there is a consistant compound growth in sales")
elif(cmpg[0]>=cmpg[1] and cmpg[1]<=cmpg[2]):
    if(cmpg[0]>=cmpg[2]):
        print("the compound sales of the company has declined in last 10 year, but the company is trying to come up with a growth of"+str(cmpg[2]-cmpg[1])+"% in last 3 years")
    else:
        print("the compound sale had a dip 5 years before but now it has recovered it")
elif(cmpg[1]>=cmpg[2]):
    print("compound sale growth of the company is decreased in last 3 years by % of ",cmpg[1]-cmpg[2])

