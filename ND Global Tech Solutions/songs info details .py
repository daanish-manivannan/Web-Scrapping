#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8


# In[2]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[3]:


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
print(df)


# In[6]:


URL=[]


# In[7]:


rows = soup.find_all(class_="panel-group")
# Extract and print the URLs
for row in rows:
    links = row.find_all("a")
    for link in links:
        href = link.get("href")
        if href:
            URL.append(href)
            #print(href)


# In[8]:


URL


# In[9]:


df['URL']=URL


# In[ ]:


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


# In[ ]:


songs=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    span_element = soup.find('span', class_='frb-description')
    for song_name in soup.find_all('span', class_='frb-description'):
        song=song_name.text
        songs.append(song)
        print(song)


# In[ ]:


#Heading
for i in songs_list_url:
    
    reqs=requests.get(i)
    sitesoup= BeautifulSoup(reqs.text,"html.parser")
    albdet=sitesoup.find('div', class_="col-xs-12 col-sm-12 col-md-4 col-lg-4 col-xl-4")
    mdlist=albdet.find('ul',class_="text-left")
    list_items = mdlist.find_all('li')
    values= []
    for item in list_items:
        span_text = item.find('span').get_text()
        text_content = item.get_text(strip=True)
        cleaned_text = text_content.replace(span_text,text_content, 1).strip()
        values.append(cleaned_text)
    mname = values[0].replace("Movie:","",1)
    mcast= values[1].replace("Cast:","",1)
    mdir= values[2].replace("Music Director:","",1)
    myr = values[3].replace("Year:","",1)
    mlabl = values[4].replace("Label:","",1)
    msingers_span=sitesoup.find('span',id="signarname")
    msingers_name = singers_span.get_text()
    print(mname)
    print(mcast)
    print(mdir)
    print(myr)
    print(mlabl)
    print(msingers_span)
    print(msingers_name)
    


# In[ ]:


df1=pd.DataFrame(songs,columns=['songs'])
print(df1)


# In[ ]:


df1['songs URL']=songs_list_url
df1


# In[ ]:


df1.to_csv(r"C:\Users\NACHI\Desktop\movie song details scraping\song_details.csv")


# In[ ]:


lyrics=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    lyricist_span=soup.find('span',id="lyricistname")
    lyricist_name = lyricist_span.get_text()
    print(lyricist_name)


# In[ ]:


singers=[]
for i in URL:
    req=requests.get(i)
    soup =BeautifulSoup(req.content,"html.parser")
    singers_span=soup.find('span',id="signarname")
    singers_name = singers_span.get_text()
    print(singers_name)

