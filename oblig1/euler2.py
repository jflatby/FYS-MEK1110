import matplotlib.pylab as plt
import numpy as np

winTime = 0
n = 100
dt = 10.0 / n

t = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)

t[0] = 0
x[0] = 0
v[0] = 0
a[0] = 5

for i in range(n-1):
    t[i+1] = t[i] + dt

    v[i+1] = v[i] + dt*a[i]
    
    a[i+1] = (400+488*np.exp(-(t[i+1]/0.67)**2)-25.8*v[i+1]-0.5*0.45*(1-0.25*np.exp(-(t[i+1]/0.67)**2)*1.293*1.2*v[i+1]**2))/80
    
    x[i+1] = x[i] + dt*v[i+1]

    if x[i+1] >= 100 and winTime == 0:
        winTime = t[i+1]
        print "Run finished in %f seconds" %(winTime)

plt.plot(t, x, t, v, t, a)
plt.legend(["Position", "Velocity", "Acceleration"])
plt.xlabel("t")
plt.ylabel("v, a, x")
plt.savefig("taskI.png")
