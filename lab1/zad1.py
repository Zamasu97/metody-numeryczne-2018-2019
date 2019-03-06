start=56
stop=100
x=[start]
y=[]
for i in range(stop-start):
    x.append(x[i]+1)
for j in range(len(x)):
    y.append(2*x[j]**2 + 2* x[j] + 2)
print(y)