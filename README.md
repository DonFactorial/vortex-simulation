# vortex-simulation
This code uses Fast Fourier Transform to solve the two-dimensional advection-diffusion equation for the vorticity $\omega(x,y,t)$ and the streamline function $\psi(x,y,t)$ and then plots the evolution of $\omega$ over time. Specifically, the equations being solved are:\
$$\omega_t+\frac{\partial\psi}{\partial x}\frac{\partial\omega}{\partial y}-\frac{\partial\psi}{\partial y}\frac{\partial\omega}{dx}=\nu\nabla^2\omega$$
$$\nabla^2\psi=\omega$$
![Heatmap of vortex simulation with four vortices of the same sign](https://github.com/DonFactorial/vortex-simulation/blob/main/four_vortices_square_heatmap.gif?raw=true)
