from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        sum = 0
        for tire_wear in self.tire_wear_sensors:
            sum = sum + tire_wear
        return sum >= 3