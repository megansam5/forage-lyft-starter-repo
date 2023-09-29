from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope_car(current_date, last_service_date, current_milage, last_service_milage):
        engine = CapuletEngine(current_milage, last_service_milage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade_car(current_date, last_service_date, current_milage, last_service_milage):
        engine = WilloughbyEngine(current_milage, last_service_milage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome_car(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach_car(current_date, last_service_date, current_milage, last_service_milage):
        engine = WilloughbyEngine(current_milage, last_service_milage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thoyex_car(current_date, last_service_date, current_milage, last_service_milage):
        engine = CapuletEngine(current_milage, last_service_milage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
