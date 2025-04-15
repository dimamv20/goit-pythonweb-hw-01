from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("vehicles")


class VehicleBasic(ABC):
    def __init__(self, brand: str, model: str, region_spec: str):
        self.brand = brand
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self): ...


class CarEngine(VehicleBasic):
    def start_engine(self):
        log.info(f"Car {self.brand} {self.model} ({self.region_spec}) — car acted.")


class Motorcycle(VehicleBasic):
    def start_engine(self):
        log.info(
            f"Motorcycle {self.brand} {self.model} ({self.region_spec}) — motorcycle acted."
        )


class AbstractVehicleFactory(ABC):
    @abstractmethod
    def build_car(self, brand: str, model: str): ...

    @abstractmethod
    def build_motorcycle(self, brand: str, model: str): ...


class AmericanFactory(AbstractVehicleFactory):
    def build_car(self, brand: str, model: str):
        return CarEngine(brand, model, "US Spec")

    def build_motorcycle(self, brand: str, model: str):
        return Motorcycle(brand, model, "US Spec")


class EuropeanFactory(AbstractVehicleFactory):
    def build_car(self, brand: str, model: str):
        return CarEngine(brand, model, "EU Spec")

    def build_motorcycle(self, brand: str, model: str):
        return Motorcycle(brand, model, "EU Spec")


if __name__ == "__main__":
    us_factory = AmericanFactory()
    eu_factory = EuropeanFactory()

    car_chevrolet = us_factory.build_car("Chevrolet", "Camaro")
    motorcycle_bmw = eu_factory.build_motorcycle("BMW", "R1250")

    car_chevrolet.start_engine()
    motorcycle_bmw.start_engine()
