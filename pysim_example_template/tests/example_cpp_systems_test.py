"""Some tests for the example cpp systems"""

from pysim.simulation import Sim
from pysim_example_template.systems.example_cpp_systems import ExampleSystem

def test_example_system():
    """Test the example system against a known solutin"""
    sys = ExampleSystem()
    sim = Sim()
    sim.add_system(sys)
    sim.simulate(5,0.1)
    assert abs(sys.states.x - 0.609483796797075) < 1e-14
