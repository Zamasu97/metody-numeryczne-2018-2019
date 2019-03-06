from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt

print('Insert desired length of the chart:')
n = int(input())/2
start=-10
stop=10
x=linspace(start,stop,200)
y=x**2
plt.plot(x,y)
plt.xlim(-n,n)
plt.show()
