from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

#reading the excel file of the raw data and storing as a data frame df

df = pd.read_excel (r'Data\data16g.xls', sheet_name='Raw Data')

x_accel = list(df['x accel'])       #creates a list from a data frame of the rows underneath the coloumn labelled x accel from excel
y_accel = list(df['y accel'])       #creates a list from a data frame of the rows underneath the coloumn labelled y accel from excel
z_accel = list(df['z accel'])       #creates a list from a data frame of the rows underneath the coloumn labelled y accel from excel

i = 0                    #setting the iteration variable, i
window_size = 3         #defining the moving average window size for the x,y,z data 
x_avg = []                                      #defining a list x_avg to store the average values as the moving average moves through x_accel
while i < len(x_accel) - window_size + 1:       #loop that will iterate current_window of window_size through x_accel
    current_window = x_accel[i : i + window_size]       #storing current_window with the current [x_accel[i], x_accel[i+1], x_accel[i+2]]
    x_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of x_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(x_accel) - window_size + 1

i = 0
while i < window_size - 1:
    x_accel.pop()                                   #removing the last 2 values from the list x_accel 
    i += 1                                          #this is to make x_accel and x_avg the same size so it can be plotted

# applying a moving avg filter to the y-axis acceleration data

i = 0                    #resetting the iteration variable, i 
y_avg = []                                      #defining a list y_avg to store the average values as the moving average moves through y_accel
while i < len(y_accel) - window_size + 1:       #loop that will iterate current_window of window_size through y_accel
    current_window = y_accel[i : i + window_size]       #storing current_window with the current [y_accel[i], y_accel[i+1], y_accel[i+2]]
    y_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of y_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(y_accel) - window_size + 1

i = 0
while i < window_size - 1:
    y_accel.pop()                                   #removing the remainder values from the list y_accel 
    i += 1                                          #this is to make y_accel and y_avg the same size so it can be plotted


# applying a moving avg filter to the z-axis acceleration data

i = 0                    #resetting the iteration variable, i
z_avg = []                                      #defining a list z_avg to store the average values as the moving average moves through z_accel
while i < len(z_accel) - window_size + 1:       #loop that will iterate current_window of window_size through y_accel
    current_window = z_accel[i : i + window_size]       #storing current_window with the current [z_accel[i], z_accel[i+1], z_accel[i+2]]
    z_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of z_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(z_accel) - window_size + 1

i = 0
while i < window_size - 1:
    z_accel.pop()                                   #removing the remainder values from the list z_accel 
    i += 1                                          #this is to make z_accel and z_avg the same size so it can be plotted

x = list(range(1,len(x_accel)+1))                     #creates a list from 1 to the length of x_accel

# plotting the acceleration data sets
fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True)       #creates a figure with 3 subplots 
ax[0].plot(x, x_accel, label = 'Raw Data')                  #plottig x, x_accel on the top sublot, labelling it raw data
ax[0].plot(x, x_avg, label = 'Filtered Data')               #plottig x, x_avg on the top sublot, labelling it filtered data
ax[1].plot(x, y_accel, label = 'Raw Data')                  #plottig y, y_accel on the middle sublot, labelling it raw data
ax[1].plot(x, y_avg, label = 'Filtered Data')               #plottig y, y_avg on the middle sublot, labelling it filtered data
ax[2].plot(x, z_accel, label = 'Raw Data')                  #plottig z, z_accel on the bottom sublot, labelling it raw data
ax[2].plot(x, z_avg, label = 'Filtered Data')               #plottig z, z_avg on the bottom sublot, labelling it filtered data

ax[0].set_title('Acceleration in the x-Direction')          #labelling the top subplot title
ax[1].set_title('Acceleration in the y-Direction')          #labelling the middle subplot title
ax[1].set_ylabel('Acceleration [g]')                        #labelling the middle subplot along the y-axis
ax[2].set_title('Acceleration in the z-Direction')          #labelling the bottom subplot title
ax[2].set_xlabel('Sample Number [n]')                       #labelling the bottom subplot along the x-axis

plt.legend()                                                #adding a legend for the raw data and filtered data to the bottom sublot
plt.tight_layout()                                          #reduces the space between the sublots
plt.show()                                                  #shows the plot using matplotlib