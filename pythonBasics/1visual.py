import matplotlib.pyplot as plt
import numpy as np

#x = [1,2,3,4,5,6,7,8]
#y = [0.1,0.2,0.5,0.8,0.9,0.6,0.3,1.4]
#plt.plot(x,y)
#plt.show()

x= np.arange(0,11)
y1 = np.cos(x)-1
y2 = 2*np.sin(x/3.)
y3 = (x**2)/20. -2
plt.plot(x,y1,c='blue')
plt.plot(x,y2,c ='black')
plt.plot(x,y3,c = 'g')
plt.show()