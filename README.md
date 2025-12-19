# vortex-simulation
This code uses Fast Fourier Transform to solve the two-dimensional advection-diffusion equation for the vorticity $\omega(x,y,t)$ and the streamline function $\psi(x,y,t)$ and then plots the evolution of $\omega$ over time. Specifically, the equations being solved are
```math
\omega_t+\psi_x\omega_y-\psi_y\omega_x=\nu\nabla^2\omega
```

```math
\nabla^2\psi=\omega
```

with periodic boundary conditions on the domain $x,y\in[-10,10]$ and the following initial condition:
```math
\omega(x,y,0)=e^{-\frac{(x+3)^2}{5}-\frac{(y+3)^2}{5}}+e^{-\frac{(x-3)^2}{5}-\frac{(y+3)^2}{5}}+e^{-\frac{(x+3)^2}{5}-\frac{(y-3)^2}{5}}+e^{-\frac{(x-3)^2}{5}-\frac{(y-3)^2}{5}}
```

which forms a "square" of vortices spinning in the same direction. Gaussian functions are a convenient choice to represent a vortex. In this simulation, we take the parameter $\nu=0.001$, the small value helps numerical stability. For the method, we take the two-dimensional Fourier transform in $x$ and $y$ to obtain the transformed equations
```math
\hat{\omega}_t=-\widehat{\psi_x\omega_y}+\widehat{\psi_y\omega_x}-\nu(k_x^2+k_y^2)\hat{\omega}
```

```math
\hat{\psi}=-\frac{\hat{\omega}}{k_x^2+k_y^2}
```

The first equation is now an ordinary differential equation in time that can be solved numerically using normal methods for ODEs. Note that the nonlinear terms haven't been transformed, as these products would become convolutions. Computationally, it is better to take the inverse transforms, compute them in the original solution space, then transform it back to Fourier space. We can now follow a procedure to step forward in time in the first equation:
1. Solve the second equation to obtain $\hat{\psi}$.
2. Calculate the nonlinear terms in the original solution space, then convert back to Fourier space.
3. Use $\hat{\psi}$ and the transformed nonlinear terms to calculate the next $\hat{\omega}_t$.
![Heatmap of vortex simulation with four vortices of the same sign](https://github.com/DonFactorial/vortex-simulation/blob/main/four_vortices_square_heatmap.gif?raw=true)
![Wireframe of vortex simulation with four vortcies of the same sign](https://github.com/DonFactorial/vortex-simulation/blob/main/four_vortices_square_wireframe.gif?raw=true)
