#%% md
# UK RAILWAY TICKETS SALES & JOURNEY ANALYSIS (EDA)
#%%
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%% md
# import data
#%%
data = pd.read_csv("C:\\Users\\pavan\\Downloads\\project datasets\\UK+Train+Rides\\railway.csv")
#%%
data.head()
#%%
data.tail()
#%%
data.shape
#%%
data.columns

#%% md
# data cleaning
#%%
data["Railcard"] = data["Railcard"].fillna(data["Railcard"].mode()[0]) # mode = Adult
data["Reason for Delay"] =data["Reason for Delay"].fillna("no delay")
data["Actual Arrival Time"]=data["Actual Arrival Time"].fillna(data["Actual Arrival Time"].mode()[0])#mode=19:05:00
# change into date or time
data["Date of Purchase"] = pd.to_datetime(data["Date of Purchase"])
data["Date of Journey"] = pd.to_datetime(data["Date of Journey"])
data["Actual Arrival Time"] = pd.to_datetime(data["Actual Arrival Time"],format="%H:%M:%S")
data["Time of Purchase"] = pd.to_datetime(data["Time of Purchase"],format="%H:%M:%S")
data["Departure Time"] = pd.to_datetime(data["Departure Time"],format="%H:%M:%S")
data["Arrival Time"] = pd.to_datetime(data["Arrival Time"],format="%H:%M:%S")
#%%
data.info()
#%% md
# feature engineering
#%%
data["month"] = data["Date of Journey"].dt.month
data["hour"] = data["Time of Purchase"].dt.hour
data["delay minutes"] = (data["Actual Arrival Time"] - data["Arrival Time"]).dt.total_seconds()/60
#%% md
# What is the overall trend of ticket purchases over time (by month)
#%%
month_sales = data.groupby('month')["Transaction ID"].count()
plt.figure(figsize = (10,5))
month_sales.plot(kind='line')
plt.title('total sold by month wise')
plt.xlabel('Month')
plt.ylabel('tickets sold')
plt.show()
#%% md
# Which Departure–Arrival routes are top 10 most frequently travelled
#%%
data["route"] = data["Departure Station"]+ "-" + data["Arrival Destination"]
routes = data["route"].value_counts().head(10)
plt.figure(figsize = (13,7))
routes.plot(kind='bar')
plt.xticks(rotation=90)
plt.title('top 10 routes')
plt.xlabel('route')
plt.show()
#%% md
# Which Ticket Class and Ticket Type generate the highest total revenue
#%%
total_revenue =(data.groupby(["Ticket Class","Ticket Type"])["Price"]).sum()
plt.figure(figsize = (10,6))
plt.xticks(rotation=45)
plt.title('total revenue by ticket class and ticket type')
plt.xlabel('ticket class and ticket type')
plt.ylabel('total revenue')
total_revenue.plot(kind='bar')
plt.show()
#%% md
# How does ticket price vary based on Ticket Class and Railcard usage
#%%
plt.figure(figsize = (10,10))
sns.boxplot(data = data,x="Ticket Class",y="Price",hue="Railcard")
plt.xticks(rotation=0)
plt.show()
#%% md
# refund requested by delay or cancelled?
#%%
plt.figure(figsize = (10,6))
sns.countplot(x="Journey Status", hue='Refund Request', data=data)
plt.title("Refund Requests vs Journey Status")
plt.show()
#%% md
# journey status distribution
#%%
status_counts = data["Journey Status"].value_counts()
plt.figure(figsize = (10,6))
plt.pie(status_counts, labels=status_counts.index,autopct='%1.1f%%')
plt.title("Journey Status")
plt.show()
#%% md
# what time of day are delays most occur?
#%%
plt.figure(figsize = (13,6))
sns.barplot(x='hour', y='delay minutes', data=data)
plt.title("Delay vs Hour of Purchase")
plt.show()
#%% md
# 