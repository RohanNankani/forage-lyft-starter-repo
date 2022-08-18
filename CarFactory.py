from batteries.SpindlerBattery import SpindlerBattery
from car import Car
from engines.CapuletEngine import CapuletEngine
from engines.SternmanEngine import SternmanEngine
from engines.WilloughbyEngine import WilloughbyEngine


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        car = Car(capuletEngine, spindlerBattery)
        return car 

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        car = Car(willoughbyEngine, spindlerBattery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_on):
        sternmanEngine = SternmanEngine(warning_light_on)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        car = Car(sternmanEngine, spindlerBattery)
        return car

    def create_rorshach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbinBattery(last_service_date, current_date)
        car = Car(willoughbyEngine, nubbinBattery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbinBattery(last_service_date, current_date)
        car = Car(capuletEngine, nubbinBattery)
        return car 
    

          


