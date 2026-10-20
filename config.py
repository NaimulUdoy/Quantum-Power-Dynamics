"""
Configuration parameters for Power System Dynamic Analysis using Quantum ODE solvers.
"""
import numpy as np

# Synchronous Generator Parameters (Multi-machine or single-machine infinite bus)
INERTIA_H = 3.5      # Inertia constant (s)
DAMPING_D = 1.0      # Damping coefficient (p.u.)
FREQ_SYNC = 2 * np.pi * 60.0  # Synchronous angular frequency (rad/s)

# State-Space Representation of Swing Equations: dx/dt = A*x + B*u
# States: x = [Delta_delta (rotor angle deviation), Delta_omega (speed deviation)]
# Matrix A construction for linearized swing dynamics
A_MATRIX = np.array([
    [0.0, 1.0],
    [-50.0, -2.5]  # Derived from synchronizing power coefficient and damping
])

# Simulation time settings
TIME_STEP = 0.01
TOTAL_TIME = 2.0
STEPS = int(TOTAL_TIME / TIME_STEP)