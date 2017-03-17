
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')


# In[2]:

import datetime
import pandas as pd


# In[ ]:




# In[3]:

def format_salary(value):
    return float(value.replace("R$ ", "").replace(".", "").replace(",", "."))


# In[4]:

df = pd.read_csv("../data/2017-03-11-salary.csv", parse_dates=['as_of'])


# In[5]:

df['gross_salary'] = df.gross_salary.apply(format_salary)
df['net_salary'] = df.net_salary.apply(format_salary)


# In[ ]:




# In[6]:

# salários negativos
df[(df.gross_salary <= 0) | (df.net_salary <= 0)]


# In[7]:

df = df[-((df.gross_salary <= 0) | (df.net_salary <= 0))].copy()


# In[ ]:




# In[ ]:




# In[8]:

df.gross_salary.plot(kind='hist', bins=30, grid=True, figsize=(10, 8))


# In[ ]:




# In[9]:

df.gross_salary.describe()


# In[ ]:




# In[10]:

df.net_salary.describe()


# In[ ]:




# ## Super salários

# In[11]:

max_salary = 24165.87


# In[12]:

super_salaries = df[df.gross_salary > max_salary]


# In[13]:

super_salaries.sort_values(by='gross_salary', ascending=False)


# In[ ]:



