EDA project : Bikeshare

### Date created
Creation date : 29th Jan 2026

### Project Title
Bikeshare Dataseet Analysis

### Description
In this project, I designed and implemented a Python-based data analysis pipeline to ingest, process, and analyze bike-share datasets for three major U.S. cities—Chicago, New York City, and Washington. 
The solution includes robust data loading, transformation, and aggregation logic to compute key descriptive metrics and usage patterns. 
Additionally, I developed an interactive, command-line–driven interface that enables dynamic filtering and on-demand analytics, demonstrating practical data engineering skills in data ingestion, validation, transformation, and user-facing analytics delivery.

### Files used
Dataset : 
washington.csv
new_york_city.csv
chicago.csv

Python code : 
bikeshare.py

### Running the code: ß
workspace root$ python bikeshare.py 

Hello! Let's explore some US bikeshare data!

Enter city (Chicago, New York City, Washington): Chicago

Enter month (all, January, February, ... June): Januaury

❌ Invalid month. Please try again.


Enter month (all, January, February, ... June): January

Enter day (all, Monday, Tuesday, ... Sunday): Monday
----------------------------------------

Calculating The Most Frequent Times of Travel...
ßßßßß
Most Common Month: 1
Most Common Day of Week: Monday
Most Common Start Hour: 17

This took 0.0013840198516845703 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

Most Common Start Station: Clinton St & Washington Blvd
Most Common End Station: Clinton St & Washington Blvd
Most Frequent Trip: Michigan Ave & Lake St -> Canal St & Madison St

This took 0.3114750385284424 seconds.
----------------------------------------

Calculating Trip Duration...

Total Travel Time: 2247180
Mean Travel Time: 639.857630979

This took 0.0005240440368652344 seconds.
----------------------------------------

Calculating User Stats...


User Types:
Subscriber    3408
Customer       104
Name: User Type, dtype: int64

Gender:
Male      2728
Female     687
Name: Gender, dtype: int64

Earliest Birth Year: 1934
Most Recent Birth Year: 1999
Most Common Birth Year: 1989

This took 0.004340410232543945 seconds.
----------------------------------------

Would you like to see 5 lines of raw data? Enter yes or no

### Credits
Udacity Nanodegree project