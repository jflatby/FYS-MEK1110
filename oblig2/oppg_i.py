import numpy as np
import matplotlib.pylab as plt

m = 0.1
k = 20
g = 9.81
L0 = 1.0
N = 10000 

v0 = 0.0   
theta0 = 30*(180.0/np.pi)      
T = 10
dt = (float(T) / N)

t = np.zeros((N,1))
r = np.zeros((N,2))
a = np.zeros((N,2))
v = np.zeros((N,2))
S = np.zeros((N,2))
G = np.zeros((N,2))

#Original
#r[0,0] = L0*np.sin(theta0)
#r[0,1] = L0*np.cos(theta0)

#Oppg m
v[0, 1] = 6.0
r[0,0] = -1.0


def rope(r, i):
    norm_r = np.linalg.norm(r)
    if norm_r < L0:
        print "Rope compressed"
        return 0
    else:
        return -k*(norm_r - L0)*r

for i in range(N-1):
    G[i,1] = -m*g
    a[i,:] = (G[i,:] + rope(r[i,:], i))/m
    v[i+1,:] = v[i,:] + a[i,:]*dt
    r[i+1,:] = r[i,:] + v[i+1,:]*dt


a[-1,:] = a[-2,:]

plt.plot(r[:,0],r[:,1])
plt.title('position')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend('r')

plt.show()
