#zad 2
import sys
check=True
print('Insert your value here:')
try:
    n = int(input())
except ValueError:
    print("Provided number is not integrer, cant calculate the factorial!")
    check=False
while (check==True):
    if (n<0):
        print('n<0, cant calculate the factorial!')
    else:
        silnia=1
        for i in range(2,n+1):
            silnia=i*silnia
        print('The factorial of the inserted value is', silnia)
    check=False
