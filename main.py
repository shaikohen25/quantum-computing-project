from quantum_teleportation import run_teleportation, perform_state_tomography
from quantum_search import run_grover_search
from quantum_error_correction import create_surface_code_circuit, decode_surface_code

def main():
    """Main function to run the quantum experiments."""
    print("Running Quantum Teleportation...")
    teleportation_results = run_teleportation()
    print("Teleportation Results:", teleportation_results)
    
    print("Performing Quantum State Tomography...")
    perform_state_tomography()
    
    print("Running Grover's Search Algorithm...")
    grover_results = run_grover_search(n=2, marked_state=[0, 1])
    print("Grover's Algorithm Results:", grover_results)
    
    print("Running Quantum Error Correction...")
    surface_code_circuit = create_surface_code_circuit()
    decoded_results = decode_surface_code(surface_code_circuit, surface_code_circuit)
    print("Decoded Results:", decoded_results)

if __name__ == "__main__":
    main()