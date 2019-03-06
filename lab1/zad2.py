print('Insert your value here:')
n = int(input())
if (n<0):
    print('n<0, cant calculate the factorial!')
else:
    silnia=1
    for i in range(2,n+1):
        silnia=i*silnia
    print('The factorial of the inserted value is', silnia)
