from tire.tire import Tire

class OctoprimeTire(Tire):
    def needs_service(self):
        if sum(self.wear_and_tear) >= 3:
            return True
        return False