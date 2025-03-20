import unittest
from protocol.cryptography_module import CryptographyModule
from protocol.routing_module import RoutingModule
from protocol.deception_module import DeceptionModule
from network_simulation.simulation_engine import SimulationEngine
class TestNetworkSimulation(unittest.TestCase):
    def test_simulation_engine(self):
        crypto = CryptographyModule()
        routing = RoutingModule()
        deception = DeceptionModule()
        crypto.update_parameters([1.0, 1.0, 1.0])
        routing.update_parameters([0.5, 0.5, 0.5])
        deception.update_parameters([1.0, 1.0, 1.0])
        engine = SimulationEngine(crypto, routing, deception)
        fitness = engine.simulate_protocol()
        self.assertTrue(0.8 < fitness < 1.2)
if __name__ == "__main__":
    unittest.main()
