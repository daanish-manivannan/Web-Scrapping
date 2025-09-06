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


# In[4]:


movie_names={
    'movies':[] }
div_properties = {'class':'col-sm-3','style': 'background-color:#f9f9f9;margin:10px;'} 
div_elements = soup.find_all('div', attrs=div_properties)
for movie in soup.find_all('div',attrs=div_properties):
    link_text = movie.text
    movie_names['movies'].append(link_text)


# In[5]:


df = pd.DataFrame(movie_names)
df


# In[6]:


df


# In[7]:


URL=[]


# In[8]:


rows = soup.find_all(class_="panel-group")
# Extract and print the URLs
for row in rows:
    links = row.find_all("a")
    for link in links:
        href = link.get("href")
        if href:
            URL.append(href)
            print(href)


# In[14]:


URL


# In[9]:


df['URL']=URL


# In[10]:


df


# In[17]:


songs_list_url=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    song_url=soup.find_all(id="song_title")
    for song in song_url:
        links=song.find_all("a")
        for link in links:
            href = link.get("href")
        if href:
            songs_list_url.append(href)
            print(href)


# In[21]:


songs=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    span_element = soup.find('span', class_='frb-description')
    for song_name in soup.find_all('span', class_='frb-description'):
        song=song_name.text
        songs.append(song)
        print(song)


# In[22]:


songs


# In[24]:


df1=pd.DataFrame(songs,columns=['songs'])
df1


# In[25]:


df1['songs URL']=songs_list_url
df1


# In[26]:


df1.to_csv(r"C:\Users\NACHI\Desktop\movie song details scraping\song_details.csv")


# In[40]:


lyrics=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    lyricist_span=soup.find('span',id="lyricistname")
    lyricist_name = lyricist_span.get_text()
    print(lyricist_name)


# In[38]:


singers=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    singers_span=soup.find('span',id="signarname")
    singers_name = singers_span.get_text()
    print(singers_name)


# In[ ]:




