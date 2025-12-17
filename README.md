# UK Railway Ticket Sales & Journey Analysis (EDA)

##  Project Overview

This project performs **Exploratory Data Analysis (EDA)** on UK railway ticket sales and journey data. The goal is to understand **travel patterns, revenue trends, delays, refunds, and customer behavior** using Python data analysis and visualization libraries.

The analysis answers key business and operational questions such as:

* How ticket sales change over time
* Which routes are most frequently traveled
* Which ticket types generate the most revenue
* When delays are most common
* How delays affect refund requests

## Dataset Description

The dataset contains information related to UK train journeys, including:

* Transaction details (Transaction ID, Purchase Date & Time)
* Journey details (Departure Station, Arrival Destination, Journey Status)
* Ticket details (Ticket Class, Ticket Type, Price, Railcard)
* Time details (Departure Time, Arrival Time, Actual Arrival Time)
* Delay and refund information

## Tools & Libraries Used

* **Python**
* **Pandas** – Data manipulation
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualizations

##  Data Cleaning & Preprocessing

The following preprocessing steps were applied:

* Handled missing values using **mode** and meaningful defaults
* Converted date and time columns to proper `datetime` formats
* Created new features:

  * `month` – Month of journey
  * `hour` – Hour of ticket purchase
  * `delay minutes` – Difference between scheduled and actual arrival time


##  Key Exploratory Analysis Performed

### 1️ Monthly Ticket Sales Trend

* Line chart showing ticket purchase trends across months

### 2️ Top 10 Most Frequent Routes

* Bar chart of the most traveled departure–arrival routes

### 3️ Revenue by Ticket Class & Ticket Type

* Identifies combinations generating the highest revenue

### 4️ Ticket Price Distribution

* Boxplot showing price variation by ticket class and railcard usage

### 5️ Refund Requests vs Journey Status

* Relationship between delays/cancellations and refund requests

### 6️ Journey Status Distribution

* Pie chart of completed, delayed, and cancelled journeys

### 7️ Delay Analysis by Time of Day

* Identifies hours with the highest average delays


##  Visualizations Included

* Line charts
* Bar charts
* Box plots
* Pie charts

All visualizations are generated using **Matplotlib** and **Seaborn**.

