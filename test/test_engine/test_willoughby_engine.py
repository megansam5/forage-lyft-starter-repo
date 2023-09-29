import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_milage = 60050
        last_service_milage = 32
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_milage = 60050
        last_service_milage = 54
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())
