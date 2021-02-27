#!/usr/bin/env python
# coding: utf-8

# In[36]:


#importing modules
import pandas as pd
import os
import statistics
import csv



# In[3]:


Banks_Data = os.path.join("Resources", "Budget_data.csv")
Banks_Data_2 = os.path.join("Resources", "Banks_summary.txt")
Banks_Data_df = pd.read_csv(Banks_Data, encoding="utf8")

Banks_Data_df.head()



# In[4]:


# No Of months
months = Banks_Data_df["Date"].value_counts()

Summary_months = len(months)
Summary_months


# In[5]:


#Total p & L

Total_Profit = Banks_Data_df["Profit/Losses"].sum()
Total_Profit


# In[6]:


# Monthly Change in p & L

Delta_Profit = Banks_Data_df["Profit/Losses"].diff()
Delta_Profit 

Banks_Data_df["Change (profit)"] = Delta_Profit 

Banks_Data_df.head()


# In[7]:


# Average Delta Profit

Average = Delta_Profit.mean()

Average


# In[33]:


# Maximum Delta profit


Maximum = Delta_Profit.max()
Maximum


# In[9]:


#Location where max month occurs
Max_Month = str
Max_Row = Banks_Data_df["Change (profit)"].idxmax()


Max_Row
Max_Month = Banks_Data_df.at[Max_Row,'Date']
Max_Month


# In[10]:


# Minimum Delta profit
Minimum = Delta_Profit.min()
Minimum 


# In[11]:


#Location where min month occurs
Min_Month = str

Min_Row = Banks_Data_df["Change (profit)"].idxmin()


Min_Row
Min_Month = Banks_Data_df.at[Min_Row,'Date']
Min_Month


# In[32]:


#Bank_Data_Summarydf = pd.DataFrame({"Total Months":[Summary_months] + [""],
                                  # "Total Profit":[Total_Profit] +[""],
                                  # "Month & Maximum":[Max_Month] +[Maximum],
                                  #  "Month & Minimum":[Min_Month] +[Minimum],
                                  # "Average Change":[Average]+[""]})

Bank_Data_Summarydf = pd.DataFrame({"Field":["Total Months"] + ["Total Profit"]+["Month & Maximum"]+["Month & Minimum"]+["Average Change"], 
                                  "Values" : [Summary_months] + ["$"]+[Max_Month]+[Min_Month]+["$"],
                                   "" :["Months"]+[Total_Profit]+[Maximum]+[Minimum]+[Average]})
                                  

Bank_Data_Summarydf


# In[37]:


Bank_Data_Summarydf.to_csv("Analysis/Banks_summary.txt",
                  encoding="utf-8", index=False, header=True)


# In[ ]:




