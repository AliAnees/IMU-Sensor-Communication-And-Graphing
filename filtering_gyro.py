from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

#reading the excel file of the raw data and storing as a data frame df

df = pd.read_excel (r'Data\dataMoving_2g.xlsx', sheet_name='Raw Data')

x_gyro = list(df['x gyro'])       #creates a list from a data frame of the rows underneath the coloumn labelled x gyro from excel
y_gyro = list(df['y gyro'])       #creates a list from a data frame of the rows underneath the coloumn labelled y gyro from excel
z_gyro = list(df['z gyro'])       #creates a list from a data frame of the rows underneath the coloumn labelled y gyro from excel

# applying a moving avg filter to the x-axis angular velocity data

i = 0                    #setting the iteration variable, i
window_size = 3         #defining the moving average window size for the x,y,z data 
x_avg = []                                      #defining a list x_avg to store the average values as the moving average moves through x_gyro
while i < len(x_gyro) - window_size + 1:        #loop that will iterate current_window of window_size through x_gyro
    current_window = x_gyro[i : i + window_size]        #storing current_window with the current [x_gyro[i], x_gyro[i+1], x_gyro[i+2]]
    x_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of x_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(x_gyro) - window_size + 1

i = 0
while i < window_size - 1:
    x_gyro .pop()                                   #removing the remainder values from the list x_gyro 
    i += 1                                          #this is to make x_gyro and x_avg the same size so it can be plotted

# applying a moving avg filter to the y-axis angular velocity data

i = 0                    #setting the iteration variable, i 
y_avg = []                                      #defining a list y_avg to store the average values as the moving average moves through y_gyro
while i < len(y_gyro) - window_size + 1:        #loop that will iterate current_window of window_size through y_gyro
    current_window = y_gyro[i : i + window_size]        #storing current_window with the current [y_gyro[i], y_gyro[i+1], y_gyro[i+2]]
    y_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of x_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(y_gyro) - window_size + 1

i = 0
while i < window_size - 1:
    y_gyro .pop()                                   #removing the remainder values from the list y_gyro 
    i += 1                                          #this is to make y_gyro and y_avg the same size so it can be plotted

# applying a moving avg filter to the z-axis angular velocity data

i = 0                    #setting the iteration variable, i
z_avg = []                                      #defining a list z_avg to store the average values as the moving average moves through z_gyro
while i < len(z_gyro) - window_size + 1:        #loop that will iterate current_window of window_size through z_gyro
    current_window = z_gyro[i : i + window_size]        #storing current_window with the current [z_gyro[i], z_gyro[i+1], z_gyro[i+2]]
    z_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of x_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(z_gyro) - window_size + 1

i = 0
while i < window_size - 1:
    z_gyro .pop()                                   #removing the remainder values from the list z_gyro 
    i += 1                                          #this is to make z_gyro and z_avg the same size so it can be plotted

x = list(range(1,len(x_gyro)+1))                        #creates a list from 1 to the length of x_gyro, normally starts at 0

# plotting the angular velocity data sets
fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True)       #creates a figure with 3 subplots 
ax[0].plot(x, x_gyro, label = 'Raw Data')                   #plottig x, x_gyro on the top sublot, labelling it raw data
ax[0].plot(x, x_avg, label = 'Filtered Data')               #plottig x, x_avg on the top sublot, labelling it filtered data
ax[1].plot(x, y_gyro, label = 'Raw Data')                   #plottig y, y_gyro on the middle sublot, labelling it raw data
ax[1].plot(x, y_gyro, label = 'Filtered Data')              #plottig y, y_avg on the middle sublot, labelling it filtered data
ax[2].plot(x, z_gyro, label = 'Raw Data')                   #plottig z, z_gyro on the bottom sublot, labelling it raw data
ax[2].plot(x, z_avg, label = 'Filtered Data')               #plottig z, z_avg on the bottom sublot, labelling it filtered data

ax[0].set_title('Angular Velocity About the x-Axis')        #labelling the top subplot title
ax[1].set_title('Angular Velocity About the y-Axis')        #labelling the middle subplot title
ax[1].set_ylabel('Angular Velocity [degrees/s]')            #labelling the middle subplot along the y-axis
ax[2].set_title('Angular Velocity About the z-Axis')        #labelling the bottom subplot title
ax[2].set_xlabel('Sample Number [n]')                       #labelling the bottom subplot along the x-axis

plt.legend()                                                #adding a legend for the raw data and filtered data to the bottom sublot
plt.tight_layout()                                          #reduces the space between the sublots
plt.show()                                                  #shows the plot using matplotlib