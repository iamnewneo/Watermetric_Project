
# coding: utf-8

# In[1]:

import bs4
import requests


# In[2]:

import pprint


# In[3]:

import time


# In[4]:

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}


# In[5]:

#just add to this list for each new player
#player name : url
query = "https://www.google.co.in/search?q=%22yamuna+clean%22&tbm=nws&start="


# In[6]:

#page = 0


# In[7]:

#page = 0
total = []
results = []
news_source_links = []
for page in range(0,400,10):
    print(query + str(page))
    req  = requests.get(query + str(page), headers=headers)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    news_stories = soup.findAll("div", { "class" : "_cnc" })
    for news in news_stories:
        single_news= {}
        single_news["news_link"] = news.find("a")["href"]
        single_news["news_title"] = news.find("a").get_text()
        single_news["news_text"] = news.find("div", {"class": "st"}).get_text()
        sourceAndTime = news.contents[1].get_text().split("-")
        single_news["news_source"], single_news["news_time"] = sourceAndTime[0], "-".join(sourceAndTime[1:])
        results.append(single_news)
        news_source_links.append(single_news["news_link"])
        #page = page + 10
        time.sleep(1)
        #print(single_news)
        #print("\n")
    #print(type(news_stories))


# In[8]:

#results


# In[19]:

#news_source_links


# ### Run individual crawlers for websites

# In[10]:

#results[0]


# In[11]:

def times_of_india(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("div", class_="Normal")
    for element in article_header:
        article_text += element.get_text()
    #print(article_header)
    return article_text

def the_hindu(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("div", class_="articleLead")
    data=soup.find_all("p", class_="body")
    #for element in article_header:
        #article_text += element.get_text()
    for element in data:
        article_text += element.get_text()
    return article_text

def daily_mail(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("p", class_="mol-para-with-font")
    for element in article_header:
        article_text += element.get_text()
    return article_text

def ndtv(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("div", class_="ins_storybody")
    for element in article_header:
        article_text += element.get_text()
    return article_text

def hindustan_times(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("p")
    for element in article_header:
        article_text += element.get_text()
    return article_text

def indian_express(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("p")
    for element in article_header:
        article_text += element.get_text()
    return article_text

def first_post(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("div", class_="fullCont1")
    for element in article_header:
        article_text += element.get_text()
    return article_text

def economic_times(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    article_header=soup.find_all("div", class_="mod-economictimesarticletextwithadcpc mod-economictimesarticletext mod-articletext")
    for element in article_header:
        article_text += element.get_text()
    return article_text

def india_today(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    #article_header=soup.find_all("div", class_="story_body_text")
    article_header=soup.findAll("div", class_="right-story-container")
    for element in article_header:
        article_text += element.get_text()
    return article_text
def other_site(src):
    page  = requests.get(src, headers=headers)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    article_text = ""
    body_with_html=soup.find("body")
#     for element in article_header:
#         article_text += element.get_text()
    return body_with_html


# In[12]:

#times_of_india_text("http://timesofindia.indiatimes.com/city/delhi/SC-Detail-steps-taken-to-keep-Yamuna-clean/articleshow/15525134.cms")
#the_hindu("http://www.thehindu.com/data/last-drop-drinking-water-sipping-poison/article8557720.ece")
#daily_mail("http://www.dailymail.co.uk/indiahome/indianews/article-3136522/Yamuna-cleanup-committee-plans-pump-river-water-straight-Delhi-households.html")
#indian_express("http://indianexpress.com/article/cities/chandigarh/chandigarh-e-water-atms-to-be-set-up-at-22-spots-in-city-2807861/")
#other_site("http://indianexpress.com/article/cities/chandigarh/chandigarh-e-water-atms-to-be-set-up-at-22-spots-in-city-2807861/")


# In[13]:

for result in results:
    if "timesofindia" in result["news_link"]:
        article_text = times_of_india(result["news_link"])
        result["article_text"] = article_text
    elif "thehindu" in result["news_link"]:
        article_text = the_hindu(result["news_link"])
        result["article_text"] = article_text
    elif "dailymail" in result["news_link"]:
        article_text = daily_mail(result["news_link"])
        result["article_text"] = article_text
    elif "indianexpress" in result["news_link"]:
        article_text = indian_express(result["news_link"])
        result["article_text"] = article_text
    elif "economictimes" in result["news_link"]:
        article_text = economic_times(result["news_link"])
        result["article_text"] = article_text
    elif "ndtv" in result["news_link"]:
        article_text = ndtv(result["news_link"])
        result["article_text"] = article_text
    elif "hindustantimes" in result["news_link"]:
        article_text = hindustan_times(result["news_link"])
        result["article_text"] = article_text
    elif "firstpost" in result["news_link"]:
        article_text = first_post(result["news_link"])
        result["article_text"] = article_text
    elif "indiatoday" in result["news_link"]:
        article_text = india_today(result["news_link"])
        result["article_text"] = article_text
    else:
        article_text = other_site(result["news_link"])
        result["article_text"] = article_text
    #print(result)


# In[14]:

## Research paper link
#http://link.springer.com/article/10.1007/s13201-011-0011-4


# In[15]:

#results


# In[23]:

import sys


# In[24]:

import pickle
PIK = "news_results.dat"
sys.setrecursionlimit(50000)
#data = ["A", "b", "C", "d"]
with open(PIK, "wb") as f:
    pickle.dump(results, f)


# In[25]:

# ## Read Pickle File
# with open(PIK, "rb") as f:
#     news_results =  pickle.load(f)


# In[26]:




# In[ ]:



