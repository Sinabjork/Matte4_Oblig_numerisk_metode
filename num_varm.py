import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#parametere
L = 1
T = 0.1
N = 50
N_t = 10000

h = L/N
k = T/N_t

x = np.linspace(0, L, N)
t = np.linspace(0, T, N_t)


gamma = k/(h**2)

u = np.zeros((N, N_t))

def funksjon(x):
    return np.sin(np.pi*x)

funk_verdi = funksjon(x)
u[:, 0] = funk_verdi

#Eulers eksplisitt

def next_step(u):
    for i in range(N_t - 1):
        for j in range(1, N - 1):
            u[j, i + 1] = gamma * (u[j + 1, i] - 2 * u[j, i] + u[j - 1, i]) + u[j, i]

next_step(u)

#Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, T = np.meshgrid(x, t)
wave = ax.plot_surface(X, T, u.T, cmap = cm.seismic)
fig.colorbar(wave, shrink=0.5, aspect = 5)

ax.set_xlabel('position')
ax.set_ylabel('time')
ax.set_zlabel('temperature')

plt.title("Eulers explicit solution of heat equation")
plt.show()

