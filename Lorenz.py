from numpy import array,arange
import matplotlib.pyplot as plt

#constantes

sigma = 10
r = 28
b = 8/3

#parametros

t0 = 0
t = 50
x0 = 0
y0 = 1
z0 = 0
N = 100000
h = (t - t0)/N

def fx(x,y,z):
    return sigma*(y - x)

def fy(x,y,z):
    return r*x - y - x*z

def fz(x,y,z):
    return x*y - b*z

def f(r):
    x = R[0]
    y = R[1]
    z = R[2]
    return array([fx(x,y,z), fy(x,y,z), fz(x,y,z)], float)

tpoints = arange(t0, t, h)

xpoints = []
ypoints = []
zpoints = []

R = array([x0,y0,z0], float)

for t in tpoints:
    xpoints.append(R[0])
    ypoints.append(R[1])
    zpoints.append(R[2])
    k1 = h*f(R)
    k2 = h*f(R + 0.5*h)
    k3 = h*f(R + 0.5*h)
    k4 = h*f(R + h)
    R += (k1 + 2 * k2 + 2 * k3 + k4)

plt.plot(tpoints,ypoints,linewidth=0.5,color="gray",label='Trajetória')
plt.xlabel('Tempo')
plt.ylabel('y(t)')
plt.legend()
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xpoints,ypoints,zpoints,linewidth=0.5,color="gray",label='Trajetória')
ax.scatter(x0,y0,z0,marker="o",color="r",label="Ponto inicial")

ax.legend(frameon=False)
ax.set_xlabel('Eixo $x$')
ax.set_ylabel('Eixo $y$')
ax.set_zlabel('Eixo $z$')
plt.show()