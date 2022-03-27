#Importing pre-requisite libraries/packages
import FaBo9Axis_MPU9250
import time
import sys
from xlwt import Workbook, easyxf #Package used for writing to an excel file

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

while True:
    sensitivity = raw_input("Enter 2g, 4g, 8g, and 16g: ") #Asking user for their preferred accelerometer sensitivity
    if sensitivity == "2g":
        mpu9250.configMPU9250(0x00, 0x00) #Each of these values represents pre-defined hexcode in the MPU9250 package, used to configure the sensitivity of the sensor
        break
    elif sensitivity == "4g":
        mpu9250.configMPU9250(0x00, 0x01)
        break
    elif sensitivity == "8g":
        mpu9250.configMPU9250(0x00, 0x02)
        break
    elif sensitivity == "16g":
        mpu9250.configMPU9250(0x00, 0x03)
        break
    else:
        print ("Invalid input. Please try again.") #Repeating code until valid input is given
        continue

wb = Workbook()
ws = wb.add_sheet('Raw Data') #Creating a new excel sheet with the given title
#Writing the names of all the columns at the top row of the sheet
ws.write(0,0,'x accel')
ws.write(0,1,'y accel')
ws.write(0,2,'z accel')
ws.write(0,3,'x gyro')
ws.write(0,4,'y gyro')
ws.write(0,5,'z gyro')
ws.write(0,6,'x magno')
ws.write(0,7,'y magno')
ws.write(0,8,'z magno')
for x in range(9):
    ws.col(x).width = 1001 #Giving a length of 1001 to the sheet, so that all recorded data points can fit

r = 1 #Counter for each row

try:
    endTime = time.time() + (100) #Definting a run-time of 100s
    #Writing values to each respective cell until the time limit has been reached
    while time.time() < endTime:
        accel = mpu9250.readAccel()
        ws.write(r,0, accel['x'])
        ws.write(r,1, accel['y'])
        ws.write(r,2, accel['z'])
        gyro = mpu9250.readGyro()
        ws.write(r,3, gyro['x'])
        ws.write(r,4, gyro['y'])
        ws.write(r,5, gyro['z'])
        mag = mpu9250.readMagnet()
        ws.write(r,6, mag['x'])
        ws.write(r,7, mag['y'])
        ws.write(r,8, mag['z'])
        time.sleep(0.1) #Recording data every 0.1s, or at a frequency of 10Hz
        print(r) #Printing current row
        r += 1

    #Saving the excel workbook to the hard drive
    wb.save('Data\data.xls')
    print ('Wrote data.xls')

except KeyboardInterrupt:
    sys.exit()
