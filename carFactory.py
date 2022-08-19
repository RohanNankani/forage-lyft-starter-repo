from batteries.spindlerBattery import SpindlerBattery
from car import Car
from engines.capuletEngine import CapuletEngine
from engines.sternmanEngine import SternmanEngine
from engines.willoughbyEngine import WilloughbyEngine
from batteries.nubbinBattery import NubbinBattery
from tire.carrigan import CarriganTire
from tire.octoprime import OctoprimeTire


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear):
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        carriganTire = CarriganTire(wear_and_tear)
        car = Car(capuletEngine, spindlerBattery, carriganTire)
        return car 

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        carriganTire = CarriganTire(wear_and_tear)
        car = Car(willoughbyEngine, spindlerBattery, carriganTire)
        return car

    def create_palindrome(self, current_date, last_service_date, warning_light_on, wear_and_tear):
        sternmanEngine = SternmanEngine(warning_light_on)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        carriganTire = CarriganTire(wear_and_tear)
        car = Car(sternmanEngine, spindlerBattery, carriganTire)
        return car

    def create_rorshach(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear):
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        octoprimeTire = OctoprimeTire(wear_and_tear)
        car = Car(willoughbyEngine, nubbinBattery, octoprimeTire)
        return car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear):
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        octoprimeTire = OctoprimeTire(wear_and_tear)
        car = Car(capuletEngine, nubbinBattery, octoprimeTire)
        return car 
    

          


