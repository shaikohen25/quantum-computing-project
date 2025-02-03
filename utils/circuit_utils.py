import numpy as np
from qiskit import Aer, transpile, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

def execute_circuit(circuit, noise_model=None, shots=1024):
    """Executes a given quantum circuit on the Aer simulator."""
    simulator = AerSimulator(noise_model=noise_model) if noise_model else AerSimulator()
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit, shots=shots).result()
    return result

def create_noise_model(single_qubit_error_prob=0.01, two_qubit_error_prob=0.01):
    """Creates a depolarizing noise model with given error probabilities."""
    noise_model = NoiseModel()
    single_qubit_error = depolarizing_error(single_qubit_error_prob, 1)
    two_qubit_error = depolarizing_error(two_qubit_error_prob, 2)
    noise_model.add_all_qubit_quantum_error(single_qubit_error, ['u1', 'u2', 'u3', 'id'])
    noise_model.add_all_qubit_quantum_error(two_qubit_error, ['cx'])
    return noise_model