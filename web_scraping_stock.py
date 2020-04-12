# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:55:46 2020

@author: Dell
"""
import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.screener.in/company/IRCTC/"
r = requests.get(URL) 

  
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.find(class_='six columns callout success').get_text()) 
