from tire.tire import Tire

class CarriganTire(Tire):
    def needs_service(self):
        for wear_and_tear in self.wear_and_tear:
          if wear_and_tear >= 0.9:
            return True
        return False
