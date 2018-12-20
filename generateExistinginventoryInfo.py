
# coding: utf-8

# In[456]:


import pandas as pd
import os


# In[457]:


categoryName = 'allrest' #inputPoint
filename = 'all'
dirname = 'C:\\Users\\OEM\\Documents\\' + 'todo\\' + categoryName + '\\'


# In[458]:


inventory = pd.read_csv(dirname + filename +'inven.csv')


# In[459]:


inventory = children[children['Warehouse Code'] == 'WH1']


# In[460]:


inventory


# In[461]:


info = pd.read_csv(dirname + filename + 'info.csv')


# In[462]:


info['Sell Price Ex Tax'] = [price.replace(',', '') for price in info['Sell Price Ex Tax'].tolist()]


# In[463]:


info


# In[464]:


inventory['regular_price'] = None
inventory


# In[465]:


for code in inventory['Product Code'].tolist():
    if code in info['Code'].tolist():
        price = (info[info['Code'] == code]['Sell Price Ex Tax']).tolist()[0]
        print(price)
        inventory.loc[inventory['Product Code'] == code, 'regular_price'] = price
        


# In[466]:


inventory.drop(columns = ['Warehouse Code', 'Warehouse Name', 'Warehouse Type', 'Cost Price', 'Quantity Available To Sell', 'Quantity Available To Ship', 'Quantity Reorder Balance'], inplace=True)


# In[467]:


inventory['type'] = ['simple'] * len(inventory.index)
inventory['cat'] = ['todo'] * len(inventory.index)
inventory = inventory.rename(columns={'Product Code': 'sku', 'Product Name': 'post_title', 'Warehouse Stock': 'stock'})


# In[468]:


inventory


# In[469]:


inventory.to_csv(dirname + filename + '_modified.csv')

