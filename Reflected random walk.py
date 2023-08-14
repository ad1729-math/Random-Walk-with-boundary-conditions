import numpy as np 
import matplotlib.pyplot as plt 
import numpy.random as rand
import math as m

p=0.51
A,B,t,E=200,-200,100000,1000
L=np.arange(B,A+1,1)
a=(1-p)/p

P_ev,P_odd,C=[],[],[]

for k in range(E):
    X,Y=[0],[0]
    for i in range(t):
        v=X[-1]
        if v==A:
            X[-1]=v-1 #X.append(v-1)
        elif v==B:
            X[-1]=v+1 #X.append(v+1)
        else: 
            r=rand.rand()
            if r<=p:
               X[-1]=v+1 #X.append(v+1)
            else:
               X[-1]=v-1 #X.append(v-1)
    P_ev.append(X[0]) 
    
    for i in range(t+1):
        v=X[-1]
        if v==A:
            Y[-1]=v-1 #X.append(v-1)
        elif v==B:
            Y[-1]=v+1 #X.append(v+1)
        else: 
            r=rand.rand()
            if r<=p:
                Y[-1]=v+1 #X.append(v+1)
            else:
                Y[-1]=v-1 #X.append(v-1)
    P_odd.append(Y[0])

for l in range(B,A+1):
    C.append((P_ev.count(l)+P_odd.count(l))/E)


def PDF(X,t):
    V=[]
    for y in X:
        x=(y+(1-2*p)*t)
        v=np.sqrt(2/m.pi/t)*(np.exp(-x**2/(2*t))+np.exp(-(2*A-x)**2/(2*t))+np.exp(-(x-2*B)**2/(2*t)))
        V.append(v)
    return V

def Stable(X):
    Z=(1+1/p*(a**(A-B)-1)/(a-1))
    V=[]
    for x in X:
        v=(a)**(A-x)/(Z*p)
        V.append(v)
    V[-1]=1/Z
    return V


plt.plot(L,C,'r+')
plt.plot(L,Stable(L),'b')
plt.show()