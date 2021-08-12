Live Data Plotting in Python.
This project is a prototype of live data plotting of random stock values using various pythong libraries and MySQL database.

We shall go through the libraries used here:

>> Preinstalled libs for every version
  - time
  - random
  - csv
  - itertools
>> To be downloaded
  - matplotlib
  - pandas
  - mysql.connector
  
Files Overview
 1. MySQL.py
 We start out by creating different tables of stock data for different given companies and storing them in a MySQL database. This data is then compiled into a csv file "data.csv" 
 using the library Pandas.
 2. Data_generator.py
 This file is now opened in the command prompt or terminal so that we can run different python files at the same time which is required to produce "live data". This data is now 
 updated every second into the csv file 'data.csv' which was created. Now this "live data" is later retrieved then and there in order to plot it on a graph
 3. Live_plot.py
 When we run this file the live data getting updated in the csv file 'data.csv' is retrieved using pandas and the values are getting plotted each instant in a graph using the
 library matplotlib.
 
This is a simple example of live data plotting by using data from a MySQL database using matplotlib and pandas.
Hope you had fun. Thank you!
