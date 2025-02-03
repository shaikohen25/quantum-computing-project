from qiskit import QuantumCircuit
from utils.circuit_utils import execute_circuit

def create_teleportation_circuit():
    """Creates a 3-qubit quantum teleportation circuit."""
    circuit = QuantumCircuit(3, 3)
    circuit.x(0)  # Initializing qubit 0 to |1>
    circuit.h(1)
    circuit.cx(1, 2)
    circuit.barrier()
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0, 1], [0, 1])
    circuit.barrier()
    circuit.cx(1, 2)
    circuit.cz(0, 2)
    circuit.measure(2, 2)
    return circuit

def run_teleportation():
    """Runs the teleportation circuit and returns measurement results."""
    circuit = create_teleportation_circuit()
    result = execute_circuit(circuit)
    return result.get_counts()