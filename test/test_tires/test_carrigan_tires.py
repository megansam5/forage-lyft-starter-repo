import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_sensors = [0.4, 0.8, 0.91, 0.2]
        tires = CarriganTires(tire_wear_sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensors = [0.4, 0.8, 0.89, 0.2]
        tires = CarriganTires(tire_wear_sensors)
        self.assertFalse(tires.needs_service())