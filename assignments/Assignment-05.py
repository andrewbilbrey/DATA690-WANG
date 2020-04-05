
# coding: utf-8

# ### Assignment 5
# 
# You will unzip the zip file manually in preparation for this assignment.
# 
# The link to the zip file is (you have already used it in your assignment 3):
# 
# https://ed-public-download.app.cloud.gov/downloads/CollegeScorecard_Raw_Data.zip
# 
# After unzipping, You will have all files in one folder named "CollegeScorecard_Raw_Data" 
# 
# The folder contains the yearly data files from 1996 to 2017 school years.
# 
# Your Jupyter Notebook file should not be in the CollegeScorecard_Raw_Data folder. 
# 
# I suggest you create a new folder call "Assignment4" and place the Notebook file and the data folder under it.
# 
# Assignment4/
#     - Jay.ipynb
#     - CollegeScorecard_Raw_Data/
#         - ...
#         - 'MERGED1996_97_PP.csv',
#         - 'MERGED2015_16_PP.csv',
#         - ...
#         - 'MERGED2017_18_PP.csv'
# 

# In[1]:


# <1> 
# Import libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#(Write code here)


# In[2]:


# <2>
# Find out what files are in the folder and assign the list of files to a variable for later processing
# you would need to import a library call os which stands for operating system. so place that import statement in previous cell.
# # os library also has method getcwd() to get the current working directory. since your notebook and your data files are not in 
# the same folder, you want to make sure what is the current working folder and how to access a data file in a different folder
# display the current workin directory


os.listdir()


# In[3]:


# <3> 
# os library has a method call listdir which generates a list of files in a directory/folder
# use this method to assign the contents of the data folder to a variable and display it

file_names = os.listdir()

file_names


# In[4]:


# <4> 
# The folder contains a couple of files that are not the yearly data files
# write code to remove the unwanted files from the list (Note: not from the folder in your drive)
# hint: use pop or remove functions of a list. pop and remove work differently though.

#csv_files = []

#for name in file_names:
#    if name.endswith(".csv"):
#        csv_files.append(name)
        
csv_files = [name for name in file_names if name.endswith(".csv")]

csv_files


# In[5]:


filename = "MERGED2016_17_PP.CSV"
filename[6:10]


# In[6]:


# <5> 
# Now that you have a clean list of the yearly files, you want to loop through them
# and read them into a dataframe one at a time. You only load three columns: UNITID, ADM_RATE, and TUITIONFEE_IN
# You also want to add a new column call "YEAR" to differentiate the data frames from each other.
# You would use an empty list and append the yearly dataframes to the list.
# After all data files are loaded and appended to the list, you would use Pandas to concatenate them into a 
# new single data frame.
# Note: this exercise incorporates many techques we learned before
# - list (creating an empty, append an item to the list)
# - for loop 
# - read only the needed columns from a file (using usecols option)
# - add a new column to a data frame
# - concatenate multiple dataframes into a single one
# This exercise may appear a big challenging but it worths the effort. You will learn a lot and  love it. I promise.


df_list = []

for csv_file in csv_files:
    df = pd.read_csv(csv_file, usecols = ["UNITID", "INSTNM", "ADM_RATE", "TUITIONFEE_IN"])
    df['YEAR'] = csv_file[6:10]
    df_list.append(df)
    print("processing file: ", csv_file)
    


# In[7]:


df = pd.concat(df_list)
df.sample(10)


# In[8]:


df.head(10)


# In[9]:


# <6> 
# explore the new dataframe (# of observations, varibles, head, tail, sample, missing values, statistics,etc.)


# In[10]:


# <7>
# the dataframe contains 22 years of data of all U.S. colleges.
# let's just look at UMBC
# filte/query the dataframe to retrieve only rows that belong to UMBC
# save the UMNC data to a new data frame. using a new variable 
# so that the old big data frame is still available for later use.

umbc = df[df["INSTNM"].str.contains("University of Maryland-Baltimore County")]
umbc


# In[11]:


# <8>
# Explore this UMBC dataframe (# of observations, varibles, head, tail, sample, missing values, statistics,etc.)


# In[12]:


# <9> 
# Plot UMBC's in-state tution overtime from 1996 to 2017.

umbc.plot.bar(x = "YEAR", y = "TUITIONFEE_IN", figsize= (12,8))
plt.title("UMBC Tuition")
#plt.ylable("In State Tuition")
plt.show()


# In[13]:


# <10>
# go back to 5/6/7 and modify the code to look at Johns Hopskins University instead.
# (No code to write here, you just modify the previous cells)

JHU = df[df["INSTNM"].str.contains("Johns Hopkins University")]
JHU


# In[27]:


# <11> 
# Now, we like to compare UMBC and JHU
# filte/query the dataframe to retrieve only rows that belong to UMBC orJHU
# save the UMNC/JHU data to a new data frame. using a new variable 
# so that the old big data frame is still available for later use.JHU = df[df["INSTNM"].str.contains("Johns Hopkins University")]


Join = df[(df['UNITID']==163268)| (df['UNITID']==162928)]


# In[28]:


# <12>
# Explore the new dataframe (#of observations, varibles, head, tail, sample, missing values, statistics,etc.)

Join.describe()


# In[29]:


# <13>
# Plot the in-state tuition of both UMBC and JHU over the 22 years on the same plot
# This plot will help us compare the two universities.
#Join.plot.bar(x = "YEAR", y = "TUITIONFEE_IN", figsize= (12,8))
#plt.title("UMBC vs. JHU Tuition")
#plt.ylable("In State Tuition")
#plt.show()

fig, ax = plt.subplots(figsize=(10,10))  
ax.scatter(Join['YEAR'], Join['TUITIONFEE_IN'], c=Join['UNITID'])
ax.set_title('In-State Tuition for JHU and UMBC 1996-2017', fontsize=14)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylim([0,55000])
ax.set_ylabel('Tuition', fontsize=14)
ax.grid(True)


# In[17]:


# <14> 
# document your observation/conclusion of the plot (use the following Markdown cell)


# #### Based on my observation of the plot,
# 
# #### UMBC's tuition has remained stagnant compaired to the increase in tuition fees for JHU. 

# In[18]:


# The end.

