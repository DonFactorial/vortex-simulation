# vortex-simulation
This code uses Fast Fourier Transform to solve the two-dimensional advection-diffusion equation for the vorticity $\omega(x,y,t)$ and the streamline function $\psi(x,y,t)$ and then plots the evolution of $\omega$ over time. Specifically, the equations being solved are:\
$$\omega_t+\frac{\partial\psi}{\partial x}\frac{\partial\omega}{\partial y}-\frac{\partial\psi}{\partial y}\frac{\partial\omega}{dx}=\nu\nabla^2\omega$$\
$$\nabla^2\psi=\omega$$\
with periodic boundary conditions and the following initial condition:\
$$\omega(x,y,0)=e^{-\frac{(x+3)^2}{5}-\frac{(y+3)^2}{5}}+e^{-\frac{(x-3)^2}{5}-\frac{(y+3)^2}{5}}+e^{-\frac{(x+3)^2}{5}-\frac{(y-3)^2}{5}}+e^{-\frac{(x-3)^2}{5}-\frac{(y-3)^2}{5}}$$\
which forms a "square" of vortices spinning in the same direction. Gaussian functions are a convenient choice to represent a vortex. For the method, we take the two-dimensional Fourier transform in $x$ and $y$ to obtain the 
![Heatmap of vortex simulation with four vortices of the same sign](https://github.com/DonFactorial/vortex-simulation/blob/main/four_vortices_square_heatmap.gif?raw=true)
