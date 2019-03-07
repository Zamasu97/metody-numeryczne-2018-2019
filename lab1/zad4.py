from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt

print('Insert desired length of the chart:')
n = int(input())
stop=n+1
if(n<=0):
    print('length must be >0!')
else:
    start=0
    x=linspace(start,stop,200)
    y=x**2
    plt.plot(x,y)
    plt.xlim(start,n)
    plt.show()
