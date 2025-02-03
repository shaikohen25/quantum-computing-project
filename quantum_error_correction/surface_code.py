from qiskit_qec.circuits import SurfaceCodeCircuit

def create_surface_code_circuit(d=3, T=1):
    """Creates a surface code circuit with given code distance d and time steps T."""
    surface_code = SurfaceCodeCircuit(d, T)
    return surface_code.get_circuit_list()[0]