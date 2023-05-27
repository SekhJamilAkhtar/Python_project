#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display


# In[3]:


Crimes = pd.read_csv('D:/CUSTOM WORK/Python Practice/CSV Data/Crimes.csv')
display(Crimes.head(10))


# In[5]:


crime = Crimes.drop(['ID', 'Case Number'], axis = 1)
crime


# In[6]:


crime['Date_Time'] = pd.to_datetime(crime['Date'])


# In[7]:


crime['Year'] = crime['Date_Time'].dt.year


# In[8]:


crime['Month'] = crime['Date_Time'].dt.month


# In[9]:


crime['Week_Day'] = crime['Date_Time'].dt.weekday


# In[10]:


crime['Day'] = crime['Date_Time'].dt.day


# In[11]:


crime['Hour'] = crime['Date_Time'].dt.hour


# In[13]:


crime['City_Block'] = crime['Block'].apply(lambda x:x.split()[0])


# In[14]:


crime.head(5)


# In[88]:


crime.dtypes


# # Some Insights From This DataSet

# In[26]:


#TOP 5 CRIME TYPES
((crime['Primary Type'].value_counts()/len(crime))*100).head().plot.bar()
plt.title('Top 5 Types of Crime')
plt.ylabel('Total Crimes In Percentage')


# In[27]:


# TOP 5 CRIME LOCATIONS
((crime['Location Description'].value_counts()/len(crime))*100).head().plot.bar()
plt.title('Top 5 Crime Locations')
plt.ylabel('Total Crimes In Percentage')


# In[30]:


# ARREST VS NO ARREST
(crime['Arrest'].value_counts()/len(crime)*100).plot.bar()
plt.title('Arrest Vs No Arrest')
plt.ylabel('Total Crimes In Percentage')


# In[81]:


crime_count = pd.DataFrame(crime.groupby(['Primary Type', 'Arrest']).size().sort_values(ascending = False).rename('Counts')).reset_index()
plt.figure(figsize = (10,20))
sns.barplot(y = 'Primary Type', x = 'Counts', data = crime_count, hue = 'Arrest', color = 'red')


# In[63]:


# TOP 5 CRIME TYPES WITH ARRESTS
arrests_by_crime = crime.groupby("Primary Type")["Arrest"].sum()
arrests_by_crime.sort_values(ascending=False).head().plot.bar()
plt.title('Number of Arrests by Crime Type')
plt.xlabel('Crime Type')
plt.ylabel('Number of Arrests')


# In[44]:


# PERCENTAGE OF DOMESTIC INCIDENTS
(crime['Domestic'].value_counts()/len(crime)*100).plot.bar()
plt.title('Domestic Incidents')
plt.ylabel('Total Crimes In Percentage')


# In[61]:


# DISTRICT WISE CRIME
fig = plt.figure(figsize=(10, 5))
(crime['District'].value_counts()/len(crime)*100).plot.bar()
plt.title('District Wise Crime')
plt.ylabel('Total Crimes In Percentage')


# In[60]:


# WARD WISE CRIME
fig = plt.figure(figsize=(15, 7))
(crime['Ward'].value_counts()/len(crime)*100).plot.bar()
plt.title('Ward Wise Crime')
plt.ylabel('Total Crimes In Percentage')


# In[67]:


# COMMUNITY AREA WISE CRIME
fig = plt.figure(figsize=(15, 7))
(crime['Community Area'].value_counts()/len(crime)*100).plot.bar()
plt.title('Community Area Area Wise Crime')
plt.ylabel('Total Crimes In Percentage')


# In[71]:


# TOP 5 IUCR CODE WISE CRIME 
((crime['IUCR'].value_counts()/len(crime))*100).head(5).plot.bar()
plt.title('Top 5 IUCR Codes Wise Crime')
plt.ylabel('Total Crimes In Percentage')


# In[84]:


# HOURLY CRIME RATE
fig = plt.figure(figsize=(10, 3))
(crime['Hour'].value_counts()/len(crime)*100).sort_index().plot.bar()
plt.title('Hourly Crime Rate')
plt.ylabel('Total Crimes In Percentage')


# In[ ]:




