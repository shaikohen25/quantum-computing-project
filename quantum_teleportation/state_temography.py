from qiskit import QuantumCircuit
from qiskit.quantum_info import random_statevector, DensityMatrix, state_fidelity
from qiskit_experiments.library import StateTomography
from utils.visualization import plot_density_matrix
from utils.circuit_utils import execute_circuit

def perform_state_tomography():
    """Performs quantum state tomography on a random state."""
    initial_state = random_statevector(2).data
    qc = QuantumCircuit(3, 3)
    qc.initialize(initial_state, 0)
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()
    qc.measure([0, 1], [0, 1])
    qc.barrier()
    qc.cx(1, 2)
    qc.cz(0, 2)
    
    qst_exp = StateTomography(qc)
    result = execute_circuit(qc)
    reconstructed_state = qst_exp.analysis_results("state").value
    plot_density_matrix(reconstructed_state)
    
    fidelity = state_fidelity(DensityMatrix(initial_state), reconstructed_state)
    print(f"State Fidelity = {fidelity:.5f}")