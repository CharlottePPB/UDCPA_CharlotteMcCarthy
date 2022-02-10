#!/usr/bin/env python
# coding: utf-8

# ## UCD PA - Data Analytics for Business - Final Project
# Charlotte McCarthy
# <br>10/02/2022

# In[1]:


#Importing the necessary Python packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc


# ### Importing the Data

# In[ ]:


#Optional code to connect to a database and import data directly from the database. 
#To run this code you would first need to configure your database ODBC connection and then update the code with your database connection details

connection_string = ("Server=Your_Server_Name;"
            "Database=My_Database_Name;"
            "UID=Your_User_ID;"
            "PWD=Your_Password;")

connection = pyodbc.connect(connection_string)
query = 'SELECT * TABLE'

data = pd.read_sql(query, connection)


# In[5]:


#Importing data from a csv file into a Pandas dataframe
data = pd.read_csv('C:/Users/mccarthyc1/Documents/GitHub/UDCPA_CharlotteMcCarthy/Data/supermarket_sales.csv')
data


# ### Analysing the Data

# In[ ]:


#Looking at the data type of each column
data.dtypes


# In[ ]:


#Splitting the data into seperate object and numeric dataframes
objects = data.select_dtypes('object')
numeric = data.select_dtypes(exclude = 'object')


# In[ ]:


#Using describe function on the object data
objects.describe()


# In[ ]:


#Using describe function on the object data
numeric.describe()


# In[6]:


#Convert time and date columns from Objects to date and time
data['Date'] =  pd.to_datetime(data['Date'], format='%m/%d/%Y')
data['Time'] =  pd.to_datetime(data['Time'], format='%H:%M').dt.time


# In[ ]:


#Checking for null values
data.isnull().sum()


# ### Visualising the Data

# In[17]:


#Using Seaborn and MatPlotLib to create charts
plt.figure(figsize=(15,10))
ax = sns.countplot(x='Gender', hue='Customer type', data=data , palette = 'pastel')
ax.set_xlabel("Gender", fontsize = 12)
ax.set_ylabel("Count of Transactions", fontsize = 12)
ax.set_title("Member Split by Gender", fontsize = 14)

for p in ax.patches:
   ax.annotate((p.get_height()), (p.get_x()+0.25, p.get_height()+0.01))

plt.savefig('../data/charts/Member-Split-By-Gender.png')


# In[18]:


plt.figure(figsize=(15,10))
ax = sns.countplot(x='Product line', hue='Gender', data=data , palette = 'pastel')
ax.set_xlabel("Gender", fontsize = 12)
ax.set_ylabel("Count of Transactions", fontsize = 12)
ax.set_title("Product Line Preference by Gender", fontsize = 14)

for p in ax.patches:
   ax.annotate((p.get_height()), (p.get_x()+0.25, p.get_height()+0.01))

plt.savefig('../data/charts/product-line-preference-by-gender.png')


# In[22]:


plt.figure(figsize=(14,10))
ax = sns.countplot(x='Product line', hue='Customer type', data=data , palette = 'pastel')
ax.set_xlabel("Membership Type", fontsize = 12)
ax.set_ylabel("Count of Transactions", fontsize = 12)
ax.set_title("Product Line Preference by Membership Type", fontsize = 14)

for p in ax.patches:
   ax.annotate((p.get_height()), (p.get_x()+0.25, p.get_height()+0.01))

plt.savefig('../data/charts/product-line-preference-member-type.png')


# In[10]:


data['Month'] = data['Date'].dt.month
sales = data.groupby(['Month','Product line'], as_index=False)['Total'].sum()


# In[20]:


plt.figure(figsize=(15,10))
ax = sns.lineplot(x='Month', y='Total', hue= 'Product line', data=sales , palette = 'bright')
sns.set_style("white")
ax.set_xlabel("Month", fontsize = 12)
ax.set_ylabel("Total Sales", fontsize = 12)
ax.set_title("Sales by Product Line", fontsize = 14)

plt.savefig('../data/charts/sales-product-line.png')


# In[ ]:




