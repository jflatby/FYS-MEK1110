import matplotlib.pylab as plt
import numpy as np

b_C = 0.1
m = 0.1
k = 10
w = np.sqrt(k/m)
g = 9.81

fr_s = 0.6
fr_d = 0.3

t = np.linspace(0, 2, 1000)
dt = t[1] - t[0]

u = 0.1

b = np.zeros(len(t))
x = np.zeros(len(t))
exact_x = np.zeros(len(t))
v = np.zeros(len(t))
a = np.zeros(len(t))
F = np.zeros(len(t))


x[0] = 0
exact_x[0] = 0
v[0] = 0
a[0] = 0
F[0] = 0

## Loop
for i in range(len(t)-1):
    b[i+1] = b_C + u*t[i]

    if (b[i] - x[i] - b_C) > (m*g*fr_s)/k:
        a[i+1] = (k/m)*(b[i] - x[i] - b_C) - g * fr_d
        v[i+1] = v[i] + dt * a[i+1]
        F[i+1] = k * (b[i] - x[i] - b_C)
    else:
        a[i+1] = 0
        v[i+1] = 0
        F[i+1] = 0
    
    x[i+1] = x[i] + dt * v[i+1]
    exact_x[i+1] = u*t[i] - (u/w)* np.sin(w*t[i])

plt.plot(t, F)
plt.xlabel("t")
plt.ylabel("Y")
plt.title("m = 1.0")
plt.legend(["Force", "Velocity", "Acceleration"])
#plt.savefig("oppg_t_1.png")
plt.show()
