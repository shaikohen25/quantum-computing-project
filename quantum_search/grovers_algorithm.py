from qiskit import QuantumCircuit
import numpy as np
from utils.circuit_utils import execute_circuit
from utils.visualization import plot_results

def create_grover_circuit(n, marked_state):
    """Creates Grover's search circuit for n qubits with a given marked state."""
    circuit = QuantumCircuit(n, n)
    circuit.h(range(n))
    circuit.barrier()
    
    # Oracle: Marking the desired state
    oracle = QuantumCircuit(n)
    for i in marked_state:
        oracle.x(i)
    oracle.h(n-1)
    oracle.mcx(list(range(n-1)), n-1)
    oracle.h(n-1)
    for i in marked_state:
        oracle.x(i)
    
    def diffusion_operator(circuit, n):
        """Applies the Grover diffusion operator."""
        circuit.h(range(n))
        circuit.x(range(n))
        circuit.h(n-1)
        circuit.mcx(list(range(n-1)), n-1)
        circuit.h(n-1)
        circuit.x(range(n))
        circuit.h(range(n))
    
    iterations = int(np.pi / 4 * np.sqrt(2**n))
    for _ in range(iterations):
        circuit.compose(oracle, inplace=True)
        diffusion_operator(circuit, n)
        circuit.barrier()
    
    circuit.measure(range(n), range(n))
    return circuit

def run_grover_search(n, marked_state):
    """Executes Grover's search circuit and returns the measurement results."""
    circuit = create_grover_circuit(n, marked_state)
    result = execute_circuit(circuit)
    plot_results(result.get_counts())
    return result.get_counts()
