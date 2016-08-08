"""Example systems created in Python
"""

from pysim.cythonsystem import Sys

class VanDerPol(Sys):
    """Simple example of a class representing a VanDerPol oscillator.
    """
    def __init__(self):
        self.add_state("x", "dx")
        self.add_state("y", "dy")
        self.add_input("a")
        self.add_input("b")
        self.inputs.a = 1.0
        self.inputs.b = 1.0
        self.states.x = 1.0
        self.states.y = 0.0

    def do_step(self,dummy):
        """Perform a timestep by implmenting the VanDerPol equations"""
        
        a = self.inputs.a
        b = self.inputs.b
        x = self.states.x
        y = self.states.y

        self.ders.dx = a*x*(b-y*y)-y
        self.ders.dy = x