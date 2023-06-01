from car import Car
import engine
import battery
from datetime import date


class CarFactory(Car):

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int):
        Car(engine.CapuletEngine, battery.SpindlerBattery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int):
        Car(engine.WilloughbyEngine, battery.SpindlerBattery)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        Car(engine.SternmanEngine, battery.SpindlerBattery)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int):
        Car(engine.WilloughbyEngine, battery.NubbinBattery)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int):
        Car(engine.CapuletEngine, battery.NubbinBattery)
