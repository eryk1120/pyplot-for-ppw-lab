import matplotlib.pyplot as plt
import numpy as np

Dane =[]
n=0

with open('dane.txt') as my_file:
    for line in my_file:
        Dane.append(int(line))
        n=n+1
n=n+1
X= np.arange(1,n,1)
Y=np.array(Dane, np.int32)
RA=0
for i in Dane:
    if i>0:
        RA=RA+i
    else:
        RA=RA-i
RA=RA/n/1000

print(RA)

plt.plot(X, Y, 'r')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()