from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

#reading the excel file of the raw data and storing as a data frame df

df = pd.read_excel (r'Data\dataMoving_2g.xlsx', sheet_name='Raw Data')

x_magno = list(df['x magno'])       #creates a list from a data frame of the rows underneath the coloumn labelled x magno from excel
y_magno = list(df['y magno'])       #creates a list from a data frame of the rows underneath the coloumn labelled y magno from excel
z_magno = list(df['z magno'])       #creates a list from a data frame of the rows underneath the coloumn labelled y magno from excel

i=0                                         #setting the iteration variable, i
x_magno = [i for i in x_magno if i != 0.0]      #removing the 0.0 data from x_magno 
i=0                                         #setting the iteration variable, i
y_magno = [i for i in y_magno if i != 0.0]      #removing the 0.0 data from x_magno 
i=0                                         #setting the iteration variable, i
z_magno = [i for i in z_magno if i != 0.0]      #removing the 0.0 data from x_magno 

# applying a moving avg filter to the x-axis magnetic field data

i = 0                    #resetting the iteration variable, i
window_size = 3         #defining the moving average window size for the x,y,z data 
x_avg = []                                      #defining a list x_avg to store the average values as the moving average moves through x_mango
while i < len(x_magno) - window_size + 1:       #loop that will iterate current_window of window_size through x_magno
    current_window = x_magno[i : i + window_size]       #storing current_window with the current [x_magno[i], x_magno[i+1], x_magno[i+2]]
    x_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of x_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(x_magno) - window_size + 1

i = 0
while i < window_size - 1:
    x_magno.pop()                                   #removing the remainder values from the list x_magno 
    i += 1                                          #this is to make x_magno and x_avg the same size so it can be plotted


# applying a moving avg filter to the y-axis magnetic field data

i = 0                    #resetting the iteration variable, i
window_size = 3         #defining the moving average window size for the x,y,z data 
y_avg = []                                      #defining a list y_avg to store the average values as the moving average moves through y_mango
while i < len(y_magno) - window_size + 1:       #loop that will iterate current_window of window_size through y_magno
    current_window = y_magno[i : i + window_size]       #storing current_window with the current [y_magno[i], y_magno[i+1], y_magno[i+2]]
    y_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of y_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(y_magno) - window_size + 1

i = 0
while i < window_size - 1:
    y_magno.pop()                                   #removing the remainder values from the list x_magno 
    i += 1                                          #this is to make y_magno and y_avg the same size so it can be plotted

# applying a moving avg filter to the z-axis magnetic field data

i = 0                    #resetting the iteration variable, i
window_size = 3         #defining the moving average window size for the x,y,z data 
z_avg = []                                      #defining a list z_avg to store the average values as the moving average moves through z_mango
while i < len(z_magno) - window_size + 1:       #loop that will iterate current_window of window_size through z_magno
    current_window = z_magno[i : i + window_size]       #storing current_window with the current [z_magno[i], z_magno[i+1], z_magno[i+2]]
    z_avg.append(sum(current_window)/window_size)       #appending the average  over the the current_window to the end of z_avg 
    i += 1                                              #adding 1 to the iteration variable until, i = len(z_magno) - window_size + 1

i = 0
while i < window_size - 1:
    z_magno.pop()                                   #removing the remainder values from the list x_magno 
    i += 1                                          #this is to make z_magno and z_avg the same size so it can be plotted

x = list(range(1, len(x_magno) + 1))         #creates a list from 1 to the length of x_magno, 

# plotting the angular velocity data sets
fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True)       #creates a figure with 3 subplots 
ax[0].plot(x, x_magno, label = 'Raw Data')                  #plottig x, x_mango on the top sublot, labelling it raw data
ax[0].plot(x, x_avg, label = 'Filtered Data')               #plottig x, x_avg on the top sublot, labelling it filtered data
ax[1].plot(x, y_magno, label = 'Raw Data')                  #plottig y, y_magno on the middle sublot, labelling it raw data
ax[1].plot(x, y_avg, label = 'Filtered Data')               #plottig y, y_avg on the middle sublot, labelling it filtered data
ax[2].plot(x, z_magno, label = 'Raw Data')                  #plottig z, z_magno on the bottom sublot, labelling it raw data
ax[2].plot(x, z_avg, label = 'Filtered Data')               #plottig z, z_avg on the bottom sublot, labelling it filtered data

ax[0].set_title('Magnetic Feild in the x-Direction')        #labelling the top subplot title
ax[1].set_title('Magnetic feild in the y-Direction')        #labelling the middle subplot title
ax[1].set_ylabel('Magnetic Field [uT]')                      #labelling the middle subplot along the y-axis
ax[2].set_title('Magnetic Field in the z-Direction')        #labelling the bottom subplot title
ax[2].set_xlabel('Sample Number [n]')                       #labelling the bottom subplot along the x-axis

plt.legend()                                                #adding a legend for the raw data and filtered data to the bottom sublot
plt.tight_layout()                                          #reduces the space between the sublots
plt.show()                                                  #shows the plot using matplotlib