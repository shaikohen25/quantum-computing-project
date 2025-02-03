from qiskit_qec.decoders import DecodingGraph
from utils.circuit_utils import execute_circuit
from utils.visualization import visualize_decoding_graph

def decode_surface_code(circuit, surface_code):
    """Executes a surface code circuit and decodes the results."""
    result = execute_circuit(circuit, shots=1)
    decoding_graph = DecodingGraph(surface_code)
    syndromes = decoding_graph.process_results(result)
    decoded_results = decoding_graph.decode(syndromes)
    visualize_decoding_graph(syndromes, decoded_results)
    return decoded_results
