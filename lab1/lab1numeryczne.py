from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt


#Zadanko 1

x=[56]
y=[]
for i in range(100-56):
    x.append(x[i]+1)
for j in range(len(x)):
    y.append(2*x[j]**2 + 2* x[j] + 2)
print(y)

#Zadanko 2

print('Insert your value here:')
n = int(input())
silnia=1
for i in range(1,n+1):
    silnia=i*silnia
print('The factorial of the inserted value is', silnia)

#Zadanko 3

def z3(x):
    xmin=x[0]
    index=0
    for i in range (1,len(x)):
        if (x[i]<xmin):
            xmin=x[i]
            index=i
    print('The lowest value in the provided array is', xmin, 'located on the', index, 'index')

z3([0, -10, 54, 6])

#Zadanko 4

print('Insert desired length of the chart:')
n = int(input())/2
x=linspace(-10,10,200)
y=x**2
plt.plot(x,y)
plt.xlim(-n,n)
plt.show()