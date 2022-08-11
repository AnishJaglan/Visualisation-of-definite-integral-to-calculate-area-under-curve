from numpy import trapz
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
from pylab import *
import math

#Taking width from the user:
b=int(input("Enter the width of the river : "))
#Taking points of width, depth, velocity from the user:
n=int(input("Enter the no. of points on the surface of water:  "))
w=[]
h=[]
v=[]
i=0
for i in range(int(n)):
    print("ENTER THE VALUES FOR SET ")
    print(i+1)
    a=int(input("Enter the value of point : "))
    d=float(input("Enter the value of depth for that point: "))
    e=float(input("Enter the value of velocity for that point: "))
    if(a>=0 and a<=b):
        w.append(a)
        h.append(-d)
        v.append(e)
    else :
        c=int(input("Enter the valid value for the points on the surface : "))
        w.append(c)
        h.append(d)
        v.append(e)
X_Y_Spline = make_interp_spline(w,h)
plt.plot(w,h)
# Returns evenly spaced numbers over a specified interval.
X_ = np.linspace(w[0], w[n-1], 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph
plt.plot(X_, Y_)
plt.title(" RATE OF WATER FLOW!!! ")
plt.xlabel(" DISTANCE FROM THE BANKS OF THE RIVER!!! ")
plt.ylabel(" DEPTH FROM THE RIVER SURFACE!!! ")
#Calculating the flow of river for the average velocity method.
j=0
flow=0
for j in range(len(w)-1):
    v1=(v[j]+v[j+1])/2
    flow += v1*((w[j]+w[j+1])/2)*abs(h[j+1]-h[j])

#Calculating the flow of river for the weighted velocity method.
k=0
flow1=0
for k in range(len(w)-1):
    vw = (w[k]*v[k]+w[k+1]*v[k+1])/(w[k]+w[k+1])
    flow1 += vw*((w[j]+w[j+1])/2)*abs((h[j+1])-(h[j]))


#Calculating the flow of river for the riemann sums method .
l=0
flow2=0
for l in range((len(w)-1)):
    area1 = ((w[l+1]-w[l])*(abs(h[l+1])+abs(h[l])))/2
    velocity =(v[l+1]+v[l])/3 + (v[l]*abs(h[l])+v[l+1]*abs(h[l+1]))/((abs(h[l])+abs(h[l+1]))*3)
    flow2 += area1*velocity
plt.text(20,-0.4, 'riemann sums', style='italic',bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
print("FLOW OF WATER BY THE METHOD OF AVERAGE VELOCITY!!!\n")
print(flow)
print("FLOW OF WATER BY THE METHOD OF WEIGHTED AVERAGE VELCOITY!!!\n")
print(flow1)
print("FLOW OF WATER BY THE RIEMANN SUMS METHOD!!!\n")
print(flow2)
plt.show()
