from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, wear_and_tear):
        self.wear_and_tear = wear_and_tear

    @abstractmethod
    def needs_service(self):
        pass