import numpy as np
from statistics import mean

xs = [1,2,3,4,5]
ys = [5,4,6,5,6]

xs = np.array(xs, dtype=np.float64)
ys = np.array(ys,dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):

    m = (((mean(xs)*mean(ys))-(mean(xs*ys)))/((mean(xs)**2) - (mean(xs*xs))))
    b= (mean(ys) - (m*mean(xs)))
    return m,b
m,b= best_fit_slope_and_intercept(xs,ys)


print(m,b)

regression_line = []
for x in xs:
    regression_line.append((m*x)+b)#i dont understand quite this line

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.scatter(xs, ys, color = '#003F72')
plt.plot(xs, regression_line)
plt.show()

predict_x = 7
predict_y = (m* predict_x)+b
print(predict_y)

plt.scatter(xs,ys,color='#003F72',label = 'data')
plt.plot(xs,regression_line,label = 'regression line')
plt.legend(loc =4)
plt.show()

