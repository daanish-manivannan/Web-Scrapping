#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

# sample website
sample_website='https://www.lyricstape.com/movie-directory'

# call get method to request the page
page=requests.get(sample_website)

# with the help of BeautifulSoup
# method and html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)


# In[2]:


years = soup.find_all("h4", {"class": "panel-title"})


# In[3]:


years[:10]


# In[4]:


for item in years:
  print(item.text)


# In[5]:


divs_with_movie_links = soup.find_all("div", {"class": "panel-body"})


# In[6]:


for div in divs_with_movie_links:
  print(div)
  break


# In[7]:


years_list = []
year_with_links = {}

for item in years:
  years_list.append(item.text)

for i in range(len(years_list)):
  print(years_list[i])
  links = [a["href"] for a in divs_with_movie_links[i].select("a[href]")]
  print(links)
  year_with_links[years_list[i]] = links
  text = [link.split('/')[-2] for link in links]
  print(text)


# In[8]:


year_with_links


# In[9]:


year_with_links['2023'][0]


# In[10]:


# further link
link=year_with_links['2023'][0]

# call get method to request the page
page=requests.get(link)

# with the help of BeautifulSoup
# method and html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.select("a[href]"))


# In[11]:


# song lyrics link
link="https://www.lyricstape.com/album/adipurush-ram-sita-ram-song-lyrics/1014/3064"

# call get method to request the page
page=requests.get(link)

# with the help of BeautifulSoup
# method and html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)


# In[12]:


song_name = soup.find_all("span", {"id": "song_name"})


# In[13]:


'Ram Sita Ram'


# In[14]:


lyricist_name = soup.find_all("span", {"id": "lyricistname"})
singer_name = soup.find_all("span", {"id": "signarname"})
print(lyricist_name[0].text)
print(singer_name[0].text)


# In[ ]:




