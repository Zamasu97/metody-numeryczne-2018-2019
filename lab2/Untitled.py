#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Zadanko 1

from cs50 import get_int
print("x: ")


# In[6]:


#zad1
from math import pi
import sys

def poleobwod(r1,r2):
    p1= pi*r1**2
    o1= 2*pi*r1
    k1=[p1,o1]
    p2=pi*r2**2
    o2=2*pi*r2
    k2=[p2,o2]
    return k1,k2

switch1=True
while (switch1==True):    
    print("podaj promien 1")
    try:
        r1 = float(input("r1: "))
        switch1=False
    except ValueError:
        print("Wprowadzony promien to nie liczba")
        
switch2=True
while(switch2==True):
    print("podaj promien 2")
    try:
        r2 = float(input("r2: "))
        switch2=False
    except ValueError:
        print("Wprowadzony promien to nie liczba")
        
r1 = abs(r1)
r2 = abs(r2)

k1,k2=poleobwod(r1,r2)
print("Pole 1 kola: " +str(k1[0]) +", obwod 1 kola: " +str(k1[1]))
print("Pole 2 kola: " +str(k2[0]) +", obwod 2 kola: " +str(k2[1]))


# In[5]:


#zad2
import sys

switch1=True
while (switch1==True):    
    print("podaj X")
    try:
        x = float(input("x: "))
        switch1=False
    except ValueError:
        print("Wprowadzona wartość to nie liczba")
        
switch2=True
while(switch2==True):
    print("podaj Y")
    try:
        y = float(input("y: "))
        if (y!=0):
            switch2=False
        else:
            print("pamietaj cholero nie dziel przez 0")
    except ValueError:
        print("Wprowadzon wartość to nie liczba")
        
def fun(x,y):
    case=False
    if (x%y==0):
        if (x%2==0) and (y%2==0):
            case=True
    return case

fun(x,y)


# In[4]:


#zad3
import sys

switch1=True
while (switch1==True):    
    print("podaj X")
    try:
        x = float(input("x: "))
        switch1=False
    except ValueError:
        print("Wprowadzona wartość to nie liczba")
        
switch2=True
while(switch2==True):
    print("podaj Y")
    try:
        y = float(input("y: "))
        if (y!=0):
            switch2=False
        else:
            print("pamietaj cholero nie dziel przez 0")
    except ValueError:
        print("Wprowadzona wartość to nie liczba")
        
XdYLog = 'X podzielne przez Y' if (x%y==0) else 'X niepodzielne przez Y'
print(XdYLog)


# In[9]:


#zad 4

import sys

switch1=True
while (switch1==True):    
    print("podaj X")
    try:
        x = float(input("x: "))
        switch1=False
    except ValueError:
        print("Wprowadzona wartość to nie liczba")
        
switch2=True
while(switch2==True):
    print("podaj Y")
    try:
        y = float(input("y: "))
        if (y!=0):
            switch2=False
        else:
            print("pamietaj cholero nie dziel przez 0")
    except ValueError:
        print("Wprowadzona wartość to nie liczba")
        
switch3=True
while(switch3==True):
    print("podaj do ilu miejsc po przecinku zaokrąglić")
    try:
        n = int(input("n: "))
        switch3=False
    except ValueError:
        print("Wprowadzona wartość to nie liczba")

w=x/y
print(round(w,n))


# In[35]:


#zad5

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

switch1=True
while (switch1==True):    
    print("podaj int od 1 do 3")
    try:
        n = float(input("r1: "))
        switch1=False
    except ValueError:
        print("Wprowadzony promien to nie int")

x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**2*np.exp(-0.1*R)
if (n==1):
    Z = np.cos(R)**2*np.exp(-0.3*R)
elif (n==2):
    Z = np.cos(R)**2*np.exp(-0.1*R)
    Z=-Z
elif (n==3):
    Z = np.cos(R)**3*np.exp(-0.1*R)
else:
    Z = np.cos(R)**2*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()


# In[11]:





# In[ ]:




