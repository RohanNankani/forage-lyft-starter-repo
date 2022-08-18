from batteries.spindlerBattery import SpindlerBattery
from car import Car
from engines.capuletEngine import CapuletEngine
from engines.sternmanEngine import SternmanEngine
from engines.willoughbyEngine import WilloughbyEngine


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        car = Car(capuletEngine, spindlerBattery)
        return car 

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        car = Car(willoughbyEngine, spindlerBattery)
        return car

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        sternmanEngine = SternmanEngine(warning_light_on)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        car = Car(sternmanEngine, spindlerBattery)
        return car

    def create_rorshach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbinBattery(last_service_date, current_date)
        car = Car(willoughbyEngine, nubbinBattery)
        return car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbinBattery(last_service_date, current_date)
        car = Car(capuletEngine, nubbinBattery)
        return car 
    

          


