from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Абстрактний клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make: str = make
        self.model: str = model
        self.region: str = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас Car, що наслідується від Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")


# Клас Motorcycle, що наслідується від Vehicle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")


# Абстрактна фабрика для транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


# Фабрика для Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# Оголошення змінних для фабрик
us_factory: VehicleFactory = USVehicleFactory()  # Оголошено фабрику США
eu_factory: VehicleFactory = EUVehicleFactory()  # Оголошено фабрику Європи

# Використання фабрик для створення транспортних засобів
vehicle1: Car = us_factory.create_car("Ford", "Mustang")  # Створюємо авто для США
vehicle1.start_engine()

vehicle2: Motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")  # Створюємо мотоцикл для Європи
vehicle2.start_engine()

