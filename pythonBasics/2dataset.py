import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('irisdata.txt',delimiter=';')
print(data[0:5])
code = np.genfromtxt('code.txt', delimiter='</div>')
time = data[:,][:,0]
sensors = data[:,][:,1:5]
print(sensors[0:6])
time = time -time[0]
print(time)
avg = np.mean(sensors,1)

plt.plot(time,sensors)
plt.plot(time,avg)
plt.show()

#export data
timecol = time.reshape(-1,1)
avgcol = avg.reshape(-1,1)

mydata= np.concatenate((timecol,sensors,avgcol),axis =1)#avg n time are row vectors n we need to convert into col vectors
np.savetxt('export from python.txt', mydata, delimiter=',')

plt.figure(1)
plt.plot(time,sensors[:,][:,1],'red')
plt.plot(time,avg,'blue')
plt.legend(['sensors 2','average'])
plt.xlabel('time(sec)')
plt.ylabel('values')
plt.savefig('myplot.png')
plt.show()