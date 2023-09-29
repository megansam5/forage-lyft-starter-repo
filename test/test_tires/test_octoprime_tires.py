import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_sensors = [0.7, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(tire_wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensors = [0.4, 0.6, 0.7, 0.2]
        tires = OctoprimeTires(tire_wear_sensors)
        self.assertFalse(tires.needs_service())