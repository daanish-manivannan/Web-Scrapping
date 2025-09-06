#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


req=requests.get("https://www.lyricstape.com/movie-directory")
soup =BeautifulSoup(req.content,"html.parser")
print(soup.prettify())


# In[3]:


movie_names={
    'movies':[]
}
div_properties = {'class':'col-sm-3','style': 'background-color:#f9f9f9;margin:10px;'} 
div_elements = soup.find_all('div', attrs=div_properties)
for movie in soup.find_all('div',attrs=div_properties):
    link_text = movie.text
    movie_names['movies'].append(link_text)
print(movie_names)


# In[4]:


df = pd.DataFrame(movie_names)
df


# In[12]:


rows = soup.find_all(class_="panel-group")
# Extract and print the URLs
for row in rows:
    links = row.find_all("a")
    for link in links:
        href = link.get("href")
        if href:
            print(href)


# In[ ]:




