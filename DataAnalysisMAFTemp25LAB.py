# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
https://www.met.ie/climate/available-data/
https://www.met.ie/climate/available-data/historical-data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

# Read data from csv file (source: met.ie); parse the data on the column named 'date'; data type is unicode; first 17 rows are header
# Add code
data = pd.read_csv("hly275.csv", skiprows = 17, parse_dates = ['date'], dtype = 'unicode')

# Print various array dimensions & characteristics
print(data.shape)
#print(data.dtypes)
# Print the entire table (Python will print some rows & use ... for the rest)
#print(data_athenry.head)
# Print some values to see data & datatypes
#print(data['date'][0:10])
#print(data['temp'][1000:1010])
# Another way to print a data type
#print(type(data['temp'][0]))


# Plot the temperature data vs the date
fig1 = plt.figure(figsize = (20, 12))
ax1 = fig1.add_subplot(1, 1, 1)
# Plot only some of the data - from start to stop; note some earlier data entries are empty & will need preprocessing
# Look at data .csv file to work out start & stop (& take into account header will be removed)
# Add code
start = 187506 - 19
stop = start + 744 #(31 days * 24 hours = 744 samples)
# The temperature data gets read in as type object; convert to float to use or plot
# The type of the following arrays are Panda series
# Add code
temp_data = data['temp'][start:stop].astype(float)
date_data = data['date'][start:stop]


# Add code
ax1.plot_date(date_data, temp_data, linestyle='-', linewidth=2, marker = ',', color='steelblue', markersize = 10)
ax1.xaxis.set_major_locator(mdates.DayLocator(bymonthday=[1, 5, 10, 15, 20, 25, 30]))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
ax1.set_xlim([pd.to_datetime('2025-01-01 00:00:00'), pd.to_datetime('2025-01-31 23:00:00')])
ax1.tick_params(axis='both', which='major', labelsize=20, pad=15)
ax1.set_ylabel('Temperature ($^\circ$C)', fontsize=24, labelpad=15)
ax1.set_title('Mace Head Temperature Data, January 2025', fontsize=26, pad=20)
yticks = np.arange(-5, 16, 5)
ax1.set_yticks(yticks)


# Moving Average Filter (MAF)
def moving_average(x, N):
    y = np.zeros(x.size)
    for n in range(0, x.size):
        for k in range(0, N):
            if n >= k:
                y[n] = y[n] + (1/N)*x[n-k]
                
    return y

x = np.array(temp_data)
# Add code 
y = moving_average(x, 24)
 


# Plot filtered output
# Add code
ax1.plot_date(data['date'][start:stop], y, linestyle='-', marker = ',', color = 'orange', markersize = 15)



# Fix the delay
# Plot the temperature data vs the date. Move it to the left, so it's not delayed
fig2 = plt.figure(figsize = (20, 12))
ax2 = fig2.add_subplot(111)
ax2.plot_date(date_data, temp_data, linestyle='-', marker = ',', color='steelblue', markersize = 10)
ax2.xaxis.set_major_locator(mdates.DayLocator(bymonthday=[1, 5, 10, 15, 20, 25, 30]))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
ax2.set_xlim([pd.to_datetime('2025-01-01 00:00:00'), pd.to_datetime('2025-01-31 23:00:00')])
ax2.tick_params(axis='both', which='major', labelsize=20, pad=15)
ax2.set_ylabel('Temperature ($^\circ$C)', fontsize=24, labelpad=15)
ax2.set_title('Mace Head Temperature, January 2025', fontsize=26, pad=20)
yticks = np.arange(-5, 23, 5)
ax2.set_yticks(yticks)
# plot filtered output, delayed by ~24/2
ax2.plot_date(data['date'][start:stop-11], y[11:], linestyle='-', marker = ',', color = 'orange', markersize = 15)



plt.show()
