#!/usr/bin/env python
# coding: utf-8

# In[128]:


import pandas as pd 
import numpy as np
import seaborn as sns
import missingno as msno


# In[129]:


df = pd.read_csv(r'C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\data\google playstore analysis\Google_Playstore_Apps.csv')


# In[130]:


df.head()


# In[131]:


df.info()


# In[132]:


#how many null values over there?


# In[133]:



msno.bar(df)


# In[134]:


df.isna().sum().sort_values(ascending=False)


# In[135]:


# clean the columns that has null 


# In[136]:


df['Rating'].plot(kind='box')


# In[137]:


df['Rating'].describe()


# In[138]:


mean_avg = df['Rating'].mean()


# In[139]:


df['Rating'].fillna(mean_avg, inplace=True) 


# In[140]:


#drop the rest of null values since they're just a few


# In[141]:


df.dropna(inplace=True)


# In[142]:


df.isna().sum().sort_values(ascending=False)


# In[143]:


#change objtype to datetime 


# In[144]:


df['Last Updated'] = pd.to_datetime(df['Last Updated'])
df['Last Updated']


# In[145]:


df.info()


# In[146]:


##### duplicates values 


# In[147]:


df.duplicated(subset=['App'], keep=False).sum()


# In[148]:


df.loc[df.duplicated(subset=['App'], keep=False)].sort_values(by='App')


# In[149]:


#df_copy_before_removing_duplicates = df.copy()


# In[ ]:


# keep the values with most reviews


# In[150]:


df.sort_values(by=['App', 'Reviews'], inplace=True)


# In[151]:


df.drop_duplicates(subset=["App"], inplace=True, keep='last')


# In[152]:


df.duplicated(subset=['App'], keep=False).sum()


# In[ ]:


###format the Category column


# In[158]:


df['Category'].value_counts()


# In[154]:


df['Category'] = df['Category'].str.replace('_', ' ')


# In[156]:


df['Category'] = df['Category'].str.capitalize()


# In[157]:





# In[180]:


## Create an auxiliary column 'Distribution' to determine wether an app is Free/Paid


# In[177]:


df['Distribution'] = 'Free'


# In[178]:


df.loc[df['Price'] > 0, 'Distribution'] = 'Paid'


# In[179]:





# In[181]:


##analysis


# In[182]:


#Which company has the most reviews?


# In[188]:


df.sort_values(by= 'Reviews', ascending=False).head(1)


# In[ ]:


##Which category has the most downloads


# In[194]:


df['Category'].value_counts()


# In[195]:


#to which category belongs the most expensive apps


# In[197]:


df.sort_values(by='Price', ascending=False).head()


# In[198]:


##whats the name of the most expensive game?


# In[204]:


df.query("Category == 'Game'").sort_values(by=['Price'],ascending=False).head(3)


# In[205]:


##most popular finance app


# In[206]:


df.query("Category == 'Finance'").sort_values(by=['Price'],ascending=False).head(2)


# In[207]:


##which free game has the greatest number of reviews


# In[208]:


df.query("Category == 'Game' and Price == 0").sort_values(by=['Reviews'],ascending=False).head(2)


# In[ ]:




