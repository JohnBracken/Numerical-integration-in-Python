#The following code sample is an example of performing numerical
#integration of a function with Python.


#Numeric python and plotting libraries imported.
import numpy as np
from matplotlib import pyplot as plt


#x axis points.
x = np.linspace(-4,4,1000)


#The corresponding y axis points of the function.
y = 4/(3 + x**4)


#Creat a plot of the function.
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()



#Perform numerical trapezoidal integration of the function.
integral = np.trapz(y, x)


#Print the final result of the integral.
print(integral)