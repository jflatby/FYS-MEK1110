import matplotlib.pylab as plt
import numpy as np

## Task Q
b_C = 0.1
m = 0.1
k = 100
w = np.sqrt(k/m)

t = np.linspace(0, 2, 1000)
dt = t[1] - t[0]

u = 0.1

b = np.zeros(len(t))
x = np.zeros(len(t))
exact_x = np.zeros(len(t))
v = np.zeros(len(t))
a = np.zeros(len(t))

x[0] = 0
v[0] = 0
a[0] = (u*t[0] - x[0]) * k / m
exact_x[0] = 0

## Loop
for i in range(len(t)-1):
    b[i+1] = b_C + u*t[i]
    a[i+1] = (k/m)*(b[i] - x[i] - b_C)
    v[i+1] = v[i] + dt * a[i+1]
    x[i+1] = x[i] + dt * v[i+1]
    exact_x[i+1] = u*t[i] - (u/w)* np.sin(w*t[i])

plt.plot(t, x)
plt.plot(t, exact_x)
plt.xlabel("t")
plt.ylabel("Y")
plt.legend(["Position", "Velocity", "Acceleration"])
plt.savefig("oppg_r.png")
plt.show()
