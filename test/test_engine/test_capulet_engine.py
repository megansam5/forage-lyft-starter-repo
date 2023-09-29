import unittest

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_milage = 30050
        last_service_milage = 32
        engine = CapuletEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_milage = 30050
        last_service_milage = 54
        engine = CapuletEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())
