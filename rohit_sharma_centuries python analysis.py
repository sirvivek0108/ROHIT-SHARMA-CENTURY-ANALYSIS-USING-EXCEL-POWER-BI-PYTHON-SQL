#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


df=pd.read_csv("C:/Users/sirvi/OneDrive/Desktop/complete/ROHIT SHARMA/rohit sharma excel file.csv") 
#FILE UPLOAD


# In[12]:


df.info()


# In[13]:


df.shape


# THE DATA HAS 48 ROWS AND 16 COLUMNS.

# In[14]:


pd.isnull(df)


# NO NULL VALUE DETECTED

# In[15]:


df.columns


# # DATA  CLEANING ,BINNING,INTEGRATION COMPLETES HERE.
# 

# In[ ]:





# # EDA-EXPLORATORY DATA ANALYSIS 

# In[26]:


df[['Strike Rate','Score']].describe()


# HE HAS SHOWN EXCEPTIONAL SKILLS WITH GREAT STRIKE_RATE WITH LOWEST STRIKE RATE IN TESTS AT 50.5600 AND HIGHEST STRIKE RATE AT 274 IN AN ODI WITH SRI_LANKA WITH THE HIGHEST ONE_DAY SCORE OF 264 WORLDWIDE.

# In[ ]:





# # 1.ASK NO-1 CENTURY BY POSITION

# In[ ]:





# In[29]:


bx=sns.countplot(x = 'Position',data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# CONCLUSION -HIS BATTING SKYROCKETED WHEN HE STARTED BATTING AT NO 1 POSITION.

# In[ ]:





# In[33]:


df.columns


# # 2. ask 2-century by format

# In[49]:


bx=sns.countplot(x = 'Type of Match',data=df)
for bars in bx.containers:
    bx.bar_label(bars)

conclusion-ODI FORMAT HAS MADE HIM A LEGEND WITH ONE OF THE HIGHEST NO OF CENTURIES.
# # 3. ask 3. century by venue(home,away,neutral) and match result.

# In[ ]:





# In[17]:


ax=sns.countplot(data=df,x='Result',hue='H/A/N')
for bars in ax.containers:
    ax.bar_label(bars)
sns.set(rc={'figure.figsize':(10,25)})


# In[ ]:





# In[54]:


df.columns


# In[ ]:





# # 4. century by captaincy

# In[55]:


bx=sns.countplot(x = 'Captain',data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# # ITS LIKE A DREAM COME TRUE CAPTAINCY AND CENTURIES WITH OPENING ALL TOGETHER.

# In[ ]:





# # 5. BEST YEARS OF HIS CAREER

# In[89]:





# In[91]:


bx=sns.countplot(x ='year' ,data=df)
for bars in bx.containers:
    bx.bar_label(bars)


# # 2019 was the milestone year of his life 

# # 6. strike rate as per format

# In[33]:


sales_age= df.groupby(['Type of Match'],as_index=False)['Strike Rate'].sum().sort_values(by='Strike Rate',ascending=False)
sns.barplot(x='Type of Match',y='Strike Rate',data=df)
sns.set(rc={'figure.figsize':(18,3)})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # with test average that hovers around 65 ,the odi average goes to 113,and t20 to 200 plus

# In[ ]:





# # 7. centuries by opponents

# In[ ]:





# In[34]:


bx=sns.countplot(x ='Against',data=df)
for bars in bx.containers:
    bx.bar_label(bars)
    


# he loves australian and srilankan bowlers specially on its pull shot.

# In[ ]:




