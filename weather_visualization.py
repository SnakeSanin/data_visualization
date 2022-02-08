"""

This project takes the maximum and minimum temperature in Sitka (City in Alaska)
and plots the temperature highs and lows.

"""

import csv  # import the module to work with csv
from matplotlib import pyplot as plt  # import the module for data visualization, and also give it an abbreviated name
from datetime import datetime  # import the date and time processing module

filename = 'data/sitka_weather_2018_simple.csv'  # save the csv file to a variable
with open(filename) as f:  # open our csv file and also give it an abbreviated name
    reader = csv.reader(f)  # use this method and pass it file object in argument
    # to create a data reader object for that file
    header_row = next(reader)  # function is called once to get the first line of the file containing the headers

    dates, highs, lows = [], [], []  # creating empty lists for our data
    for row in reader:  # loop through the lines in the file
        current_date = datetime.strptime(row[2], "%Y-%m-%d")  # convert data containing row[2]  to a datetime object
        high = int(row[5])  # on each pass of the cycle the value at index[5] is assigned to high
        cels = 5.0*(high - 32) / 9  # convert fahrenheit to celsius
        mins = int(row[6])  # on each pass of the cycle the value at index[5] is assigned to mins
        cels_mn = 5.0*(mins - 32) / 9  # convert fahrenheit to celsius
        dates.append(current_date)  # add current_date value to the list
        highs.append(round(cels))  # add cels value to the list
        lows.append(cels_mn)  # add cels_mn value to the list


plt.style.use('seaborn')  # style used for charting
fig, ax = plt.subplots()  # The subplots() function allows you to generate one or more subplots on a single plot.
# The variable fig represents the entire drawing or set of generated diagrams.
# The variable ax represents one chart in the figure
ax.plot(dates, highs, c='red', alpha=0.5)  # we transfer the values of dates and temperature maxima to plot()
# с='red' this is the color of the line, alpha=0.5 it is degree of transparency
plt.plot(dates, lows, c='blue', alpha=0.5)  # we transfer the values of dates and temperature minimum to plot()
# с='blue' this is the color of the line, alpha=0.5 it is degree of transparency
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # The fill_between() point passes a list of dates
# for x values and two series highs and lows values.
# The facecolor argument specifies the color of the area to be painted;
# we give it a low alpha=0.1 so that the filled area connected two series of data

plt.title('Daily high and low temperature - 2018', fontsize=24)  # our chart title and font Size
plt.xlabel('', fontsize=16)  # change font size to make labels easier to read
fig.autofmt_xdate()  # Calling fig.autofmt_xdate() renders date labels diagonally so they don't overlap.
plt.ylabel('Temperature (C)', fontsize=16)  # change font size and name the y axis
plt.tick_params(axis='both', which='major', labelsize=16)  # the tick_params() function determines the appearance
# of tick marks on the axes

plt.show()  # Calling plt.show() opens matplotlib viewer window and outputs the plot
