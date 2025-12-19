import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rhsfunc_fft(t, omegafvec, nu, KX, KY, K2, n):
    omegaf = (omegafvec[:n**2]+1j*omegafvec[n**2:]).reshape((n,n))
    psif = -omegaf/K2
    psi_x = np.real(np.fft.ifft2(1j*KX*psif))
    psi_y = np.real(np.fft.ifft2(1j*KY*psif))
    omega_x = np.real(np.fft.ifft2(1j*KX*omegaf))
    omega_y = np.real(np.fft.ifft2(1j*KY*omegaf))
    omegat = -np.fft.fft2(psi_x*omega_y)+np.fft.fft2(psi_y*omega_x)-nu*K2*omegaf
    omegatvec = omegat.reshape(n**2)
    return np.concatenate((np.real(omegatvec), np.imag(omegatvec)))

# Simulation parameters
n = 2**7
N = n**2
nu = 0.001
xspan = np.linspace(-10,10,n+1)
xspan = xspan[:-1]
yspan = np.linspace(-10,10,n+1)
yspan = yspan[:-1]
xvals, yvals = np.meshgrid(xspan, yspan)

# Getting frequencies in Fourier space
k_x = 2*np.pi/20*np.concatenate((np.arange(0,n//2),np.arange(-n//2,0)))
k_y = 2*np.pi/20*np.concatenate((np.arange(0,n//2),np.arange(-n//2,0)))
k_x[0] = 1e-6
k_y[0] = 1e-6
K_x, K_y = np.meshgrid(k_x, k_y)
K = K_x**2+K_y**2

# Initial condition: four vortices in a square
tspan = np.arange(0, 180+0.5, 0.5)
omega0 = np.exp(-(xvals+3)**2/5 - ((yvals+3)**2)/5) + np.exp(-(xvals-3)**2/5 - ((yvals+3)**2)/5) + np.exp(-(xvals+3)**2/5 - ((yvals-3)**2)/5) + np.exp(-(xvals-3)**2/5 - ((yvals-3)**2)/5)
omega0f = np.fft.fft2(omega0)
omega0fvec = omega0f.reshape(N)
omega0fvec = np.concatenate((np.real(omega0fvec), np.imag(omega0fvec)))

# Time step through equation
sol = solve_ivp(rhsfunc_fft, t_span=(tspan[0], tspan[-1]), y0=omega0fvec, t_eval=tspan, args=(nu, K_x, K_y, K, n))

# Make heatplot visualization
fig, ax = plt.subplots()
ims = []
for i in range(tspan.size):
    o = sol.y[:,i]
    o = o[:N]+1j*o[N:]
    if i==0:
        im = ax.imshow(np.real(np.fft.ifft2(o.reshape((n,n)))))
    else:
        im = ax.imshow(np.real(np.fft.ifft2(o.reshape((n,n)))), animated=True)
    ims.append([im])

ax.set_title('Four vortices in a square')
ax.axis('off')
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('four_vortices_square_heatmap.gif')

# Make wireframe visualization
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ims = []
for i in range(tspan.size):
    o = sol.y[:,i]
    o = o[:N]+1j*o[N:]
    if i==0:
        im = ax.plot_wireframe(xvals, yvals, np.real(np.fft.ifft2(o.reshape((n,n)))))
    else:
        im = ax.plot_wireframe(xvals, yvals, np.real(np.fft.ifft2(o.reshape((n,n)))), animated=True)
    ims.append([im])

ax.set_title('Four vortices in a square')
ax.view_init(elev=60, azim=45)
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
ani.save('four_vortices_square_wireframe.gif')