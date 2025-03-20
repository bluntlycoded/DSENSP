import unittest
from protocol.cryptography_module import CryptographyModule
from protocol.routing_module import RoutingModule
from protocol.deception_module import DeceptionModule
class TestProtocolModules(unittest.TestCase):
    def test_cryptography_evaluation(self):
        crypto = CryptographyModule()
        crypto.update_parameters([1.0, 1.0, 1.0])
        self.assertAlmostEqual(crypto.evaluate_security(), 1.0)
    def test_routing_evaluation(self):
        routing = RoutingModule()
        routing.update_parameters([0.5, 0.5, 0.5])
        self.assertAlmostEqual(routing.evaluate_routing(), 1.0, places=2)
    def test_deception_evaluation(self):
        deception = DeceptionModule()
        deception.update_parameters([1.0, 1.0, 1.0])
        self.assertAlmostEqual(deception.evaluate_deception(), 1.0)
if __name__ == "__main__":
    unittest.main()
