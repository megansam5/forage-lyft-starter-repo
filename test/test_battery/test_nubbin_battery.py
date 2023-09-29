import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-05-01")
        last_service_date = date.fromisoformat("2019-01-12")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-05-01")
        last_service_date = date.fromisoformat("2020-01-12")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
