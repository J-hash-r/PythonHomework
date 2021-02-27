#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import os
import statistics


# In[2]:


Poll = os.path.join('Resources', 'Election_Data.csv')

Poll_DF = pd.read_csv(Poll)
Poll_DF.head()

Poll_Data = os.path.join("Analysis", "Poll_summary.txt")


# In[3]:


pd.Candidates = Poll_DF["Candidate"].unique()

pd.Candidates


# In[4]:


CandidateNames = Poll_DF.set_index("Candidate")
CandidateNames.head()


# In[9]:




# Count of vots for ech candidate, grouping by each candidate, counting on voter id

Group = CandidateNames.groupby("Candidate")

Vote_counts = Group["Voter ID"].count()

Vote_counts
#Khanvotes = Poll_DF[Poll_DF["Candidate"]=="Khan"]
#Khan_Total = Khanvotes.value_count()

#Correyvotes = Poll_DF[Poll_DF["Candidate"]=="Correy"]
#Correy_Total = Correyvotes.sum()


#Livotes = Poll_DF[Poll_DF["Candidate"]=="Li"]
#Li_Total = Livotes.sum()

#O_Tooleyvotes = Poll_DF[Poll_DF["Candidate"]=="O'Tooley"]
#O_Tooley_Total = O_Tooleyvotes.sum()

VOTE_SUMM = pd.DataFrame(Vote_counts)
VOTE_SUMM


# In[10]:


VOTE_SUMM = VOTE_SUMM.rename(columns={"Voter ID": "Vote_Counts"})
VOTE_SUMM 


# In[7]:


# Percntage votes

Total_Votes = len(Poll_DF)
Total_Votes


# In[15]:


Percentage_Of_Vote = VOTE_SUMM["Vote_Counts"]/Total_Votes * 100
Vote_Summ2 = pd.DataFrame({"Vote_Counts":Vote_counts,
                         "Vote Percentage":Percentage_Of_Vote})

Vote_Summ2


# In[22]:


Max_Row = Vote_Summ2["Vote Percentage"].idxmax()


Max_Row

WinningVotes = Vote_Summ2.at[Max_Row,'Vote_Counts']
WinningVotes
WinningPcent = Vote_Summ2.at[Max_Row,'Vote Percentage']
WinningPcent                                 


# In[31]:


print("The Winner Of the Poular Vote and arch ruler of the land is Mr. "+ Max_Row +"!" + " Congratulation Mr." + Max_Row)


# In[32]:


Vote_Summ2.to_csv("Analysis/Vote_Summ2.txt",
                  encoding="utf-8", index=False, header=True)


# In[ ]:




