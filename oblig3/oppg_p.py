import matplotlib.pylab as plt
import numpy as np

## Task Q
b = 0.1
m = 0.1
k = 100
w = np.sqrt(k/m)

t = np.linspace(0, 2, 1000)
dt = t[1] - t[0]
x = np.zeros(len(t))
v = np.zeros(len(t))
a = np.zeros(len(t))

x[0] = 0
v[0] = 0.1
a[0] = 0

## Loop
for i in range(len(t)-1):
    a[i+1] = -k*(x[i] + b)
    v[i+1] = v[i] + dt * a[i+1]
    x[i+1] = x[i] + dt * v[i+1]

plt.plot(t, x)
plt.plot(t, v)
plt.plot(t, a)
plt.xlabel("t")
plt.ylabel("Y")
plt.legend(["Position", "Velocity", "Acceleration"])
plt.savefig("oppg_p.png")
plt.show()
