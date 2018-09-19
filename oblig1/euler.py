import numpy as np
import matplotlib.pylab as plt

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
    a[i+1] = (-0.6*1.293*0.45)/80 * v[i]**2 + 5
    v[i+1] = v[i] + dt*a[i]
    x[i+1] = x[i] + dt*v[i+1]
    t[i+1] = t[i] + dt

    if x[i+1] >= 100 and winTime == 0:
        winTime = t[i+1]
        print "Run finished in %f seconds" %(winTime)

plt.plot(t, x, t, v, t, a)
plt.legend(["Position", "Velocity", "Acceleration"])
plt.xlabel("t")
plt.ylabel("v, a, x")
plt.savefig("taskE.png")
