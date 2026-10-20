"""
Main execution script for Power System Dynamic Analysis via Quantum ODEs with Visualization and Saving.
"""
import numpy as np
import matplotlib.pyplot as plt
from config import A_MATRIX, TIME_STEP, TOTAL_TIME, STEPS
from models.quantum_ode_solver import QuantumODESolver

def main():
    print("=== Initializing Quantum Linear Differential Equation Solver ===")
    
    # Initial perturbation state: [Initial rotor angle deviation (rad), Initial frequency deviation (p.u.)]
    initial_disturbance = np.array([0.15, 0.05])
    print(f"Initial State Disturbance: Angle = {initial_disturbance[0]} rad, Frequency = {initial_disturbance[1]} p.u.")

    # Initialize Quantum ODE Solver
    solver = QuantumODESolver(A_MATRIX, TIME_STEP)
    
    print("\nSimulating transient dynamics over time horizon...")
    trajectory = solver.simulate_trajectory(initial_disturbance)

    print(f"\nSimulation complete ({TOTAL_TIME} seconds, step size {TIME_STEP}s):")
    print(f"{'Time (s)':<10} | {'Angle Deviation (rad)':<22} | {'Freq Deviation (p.u.)':<22}")
    print("-" * 62)

    for i in range(0, len(trajectory), 20):  # Print every 20th step
        t_val = i * TIME_STEP
        angle, freq = trajectory[i]
        print(f"{t_val:<10.2f} | {angle:<22.4f} | {freq:<22.4f}")

    print("\nGenerating stability trajectory plots and saving image...")
    
    # Time vector for plotting
    time_axis = np.linspace(0, TOTAL_TIME, STEPS + 1)
    angle_deviations = trajectory[:, 0]
    freq_deviations = trajectory[:, 1]

    # Create matplotlib visualization
    plt.figure(figsize=(10, 5))
    
    # Plot Rotor Angle Deviation
    plt.subplot(2, 1, 1)
    plt.plot(time_axis, angle_deviations, label='Rotor Angle Deviation ($\Delta\delta$)', color='b', linewidth=2)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.ylabel('Angle (rad)')
    plt.title('Power System Transient Stability Dynamics (Quantum ODE Solver)')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper right')

    # Plot Frequency Deviation
    plt.subplot(2, 1, 2)
    plt.plot(time_axis, freq_deviations, label='Frequency Deviation ($\Delta\omega$)', color='r', linewidth=2)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (p.u.)')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper right')

    plt.tight_layout()
    
    # Save the figure as an image file in the project folder
    output_filename = "power_system_stability_curve.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Plot successfully saved as '{output_filename}' in your project directory.")

    # Show the plot window
    plt.show()

    print("\nQuantum power system dynamic analysis and plotting finished successfully!")

if __name__ == "__main__":
    main()