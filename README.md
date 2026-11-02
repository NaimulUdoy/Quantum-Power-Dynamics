# ⚡ Quantum Power Dynamics: Transient Stability Solver

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A research framework for solving power system transient stability dynamics using **Quantum ODE Solvers**. This repository models rotor angle deviation ($\Delta\delta$) and frequency deviation ($\Delta\omega$) trajectories over time following severe grid disturbances.

---

## 📈 Key Results & Visualizations

### Power System Transient Stability Dynamics (Quantum ODE Solver)
![Stability Curve](results/power_system_stability_curve.png)

* **Rotor Angle Response:** Tracks rotor angle deviation to ensure synchronism and system stability.
* **Frequency Dynamics:** Monitors frequency deviation recovery across simulated time steps.

---

## 🗂️ Repository Structure

* `main.py` — Entry point script executing the quantum-enhanced simulation loop.
* `quantum_ode_solver.py` — Core quantum ODE algorithm implementation.
* `config.py` — Synchronous machine parameters, inertia constants, and transient boundary conditions.
* `requirements.txt` — Python package dependencies.
* `results/` — High-resolution output graphs and transient trajectory logs.

---

## 🚀 Getting Started

### Prerequisites & Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/NaimulUdoy/Quantum-Power-Dynamics.git](https://github.com/NaimulUdoy/Quantum-Power-Dynamics.git)
cd Quantum-Power-Dynamics
pip install -r requirements.txt
