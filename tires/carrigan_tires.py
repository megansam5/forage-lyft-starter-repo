from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        for tire_wear in self.tire_wear_sensors:
            if(tire_wear >= 0.9):
                return True
        return False