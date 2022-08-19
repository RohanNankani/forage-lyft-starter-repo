import unittest
from datetime import datetime
from carFactory import CarFactory
    
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_calliope(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_calliope(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [1, 0.95, 0.4, 0.2]

        car = CarFactory.create_calliope(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.6, 0.4, 0.3, 0.2]

        car = CarFactory.create_calliope(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())



class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_glissade(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_glissade(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.4, 0.9, 0.4, 0.2]

        car = CarFactory.create_glissade(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.8, 0.4, 0.3, 0.2]

        car = CarFactory.create_glissade(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_on = False
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_on = False
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_palindrome(self, today, last_service_date, warning_light_on, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_on = True
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_palindrome(self, last_service_date, last_service_date, warning_light_on, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_on = False
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_palindrome(self, last_service_date, last_service_date, warning_light_on, wear_and_tear)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        wear_and_tear = [1, 0.95, 0.4, 0.2]
        warning_light_on = False

        car = CarFactory.create_palindrome(self, last_service_date, last_service_date, warning_light_on, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        wear_and_tear = [0.6, 0.4, 0.3, 0.2]
        warning_light_on = False

        car = CarFactory.create_palindrome(self, last_service_date, last_service_date, warning_light_on, wear_and_tear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_rorshach(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_rorshach(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_rorshach(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_rorshach(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [1, 1, 0.95, 0.2]

        car = CarFactory.create_rorshach(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [1, 1, 0.3, 0.2]

        car = CarFactory.create_rorshach(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_thovex(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.7, 0.4, 0.2]

        car = CarFactory.create_thovex(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [0.5, 0.5, 1, 1]

        car = CarFactory.create_thovex(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        wear_and_tear = [1, 0.3, 1, 0.6]

        car = CarFactory.create_thovex(self, last_service_date, last_service_date, current_mileage, last_service_mileage, wear_and_tear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()