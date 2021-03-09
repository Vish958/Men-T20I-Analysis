#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv('F:\Downloads New\Men T20I Player.csv' , low_memory = False)


# In[110]:


df = pd.read_csv ('F:\Downloads New\Men T20I Player.csv')
df.head(12)


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[7]:


type(df['Innings Player'][0])


# In[8]:


type(df['Innings Runs Scored'][0])


# In[10]:


type(df['Innings Balls Faced'][0])


# In[11]:


df.info


# In[12]:


df.info(12)


# In[13]:


df['Innings Player'].value_counts(104622)


# In[16]:


df['Innings Player'].value_counts().plot(kind = 'bar')


# In[18]:


df['Innings Player'].value_counts().plot(kind = 'bar')
plt.ylabel('Runs' , color = 'red' , size = 'x-large')
plt.xlabel(' Players Name' , color = 'red' , size = 'x-large')


# In[24]:


top12 = df['Innings Player'].value_counts()
top12.sort_values(ascending=False)
top12 = top12[:12]
top12.plot(kind='bar')
plt.ylabel('Runs' , color='red' , size = 'x-large')
plt.xlabel('Players Name' , color='red' , size = 'x-large')
plt.show()


# In[26]:


top20 = df['Innings Player'].value_counts()
top20.sort_values(ascending=False)
top20 = top20[:20]
top20.plot(kind='bar')
plt.ylabel('Runs' , color='red' , size = 'x-large')
plt.xlabel('Players Name' , color='red' , size = 'x-large')
plt.show()


# In[54]:


top12 = df['Innings Player'].value_counts()
top12.sort_values(ascending=False)
top12 = top12[:12]
top12.plot(kind='pie')
plt.show()


# In[41]:


top20 = df['Innings Player'].value_counts()
top20.sort_values(ascending=False)
top20 = top20[:20]
top20.plot(kind = 'pie')
plt.show()


# In[43]:


labels = 'RG Sharma','MS Dhoni','MJ Guptil', 'V Kohli'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[64]:


df['Innings Boundary Fours'].value_counts()


# In[52]:


df['Innings Boundary Fours'].value_counts().plot(kind = 'bar')


# In[58]:


top10 = df['Innings Boundary Fours'].value_counts()
top10.sort_values(ascending=False)
top10 = top10[:10]
top10.plot(kind = 'pie')
plt.show()


# In[90]:


labels = '1' , '2' , '3' ,'4' '10'
sizes = [15, 30, 45, 60]
explode = (0, 0.2, 0, 0)  # only "explode" the 2nd slice (i.e. 'Fours')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[63]:


df['Innings Boundary Sixes'].value_counts()


# In[62]:


df['Innings Boundary Sixes'].value_counts().plot(kind = 'bar')


# In[66]:


top20 = df['Innings Boundary Sixes'].value_counts()
top20.sort_values(ascending=False)
top20 = top20[:20]
top20.plot(kind = 'pie')
plt.show()


# In[108]:


labels = '1' , '2' , '3' , '4'
sizes = [15 , 30 , 45 , 60]
explode = (0 , 0.1 , 0 , 0) # only "explode" the 2nd slice (i.e. 'Sixes')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', 
        shadow=True, startangle=90)
ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# 
