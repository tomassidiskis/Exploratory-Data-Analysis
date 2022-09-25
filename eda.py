#!/usr/bin/env python
# coding: utf-8

# In[68]:


# Netlix EDA

# Tomas Sidiskis

# Dataset available at: *https://www.kaggle.com/datasets/shivamb/netflix-shows*


# In[ ]:


# Importing libraries and data


# In[20]:


get_ipython().system(' pip install plotly')


# In[21]:


import pandas as pd
import plotly.express as px


# In[9]:


data_import = pd.read_csv("netflix_titles.csv")
data_import["date_added"] = pd.to_datetime(data_import["date_added"].str.strip(), format="%B %d,  %Y")
data_import


# In[5]:


# High level EDA


# In[12]:


data_import.dtypes


# In[ ]:


# Numerical Column Describe


# In[11]:


data_import.describe()


# In[16]:


# Date Analysis


# In[17]:


data_import["release_year"].hist() #Matplotlib version


# In[22]:


px.histogram(data_import, x="release_year") # Plotly method


# In[25]:


data_import[data_import["release_year"] == 1925]


# In[14]:


data_import["date_added"].hist() # Matplotlib Method


# In[32]:


# Extract Month from date_added

data_import["date_added_month"] = data_import["date_added"].dt.month.fillna(0)
data_import["date_added_day"] = data_import["date_added"].dt.day.fillna(0)


# In[30]:


px.histogram(data_import, x="date_added", color="date_added_month") # Histogram of dates


# In[37]:


px.histogram(data_import, x="date_added_month", color="type")


# In[38]:


px.histogram(data_import, x="date_added_day", color="type") # Looks like Netflix adds movies on the first of the month more then any other day


# In[34]:


# String Column Analysis


# In[35]:


data_import.columns


# In[36]:


data_import["type"].unique()


# In[40]:


data_import["country"].str.split(",", expand=True)


# In[55]:


country_count = data_import.copy()
country_count = pd.concat([country_count, data_import["country"].str.split(",", expand=True)], axis=1)
country_count = country_count.melt(id_vars=["type", "title"], value_vars=range(12), value_name = "Country")
country_count = country_count[country_count["Country"].notna()]
country_count["Country"] = country_count["Country"].str.strip()
country_count


# In[59]:


px.histogram(country_count, "Country", color="type").update_xaxes(categoryorder = "total descending")


# In[62]:


data_import["rating"].hist()


# In[63]:


px.histogram(data_import, "rating").update_xaxes(categoryorder = "total descending")


# In[66]:


data_import["Cast Count"] = data_import["cast"].str.split(",")
data_import = data_import[data_import["Cast Count"].notna()]
data_import["Cast Count"] = data_import["Cast Count"].apply(lambda x: len(x))
data_import


# In[67]:


px.histogram(data_import, "Cast Count").update_xaxes(categoryorder = "total descending")


# In[ ]:


# Thanks for reading

