from abc import ABC, abstractmethod

# Абстрактний клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        pass

# Клас Car, що наслідується від Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")

# Клас Motorcycle, що наслідується від Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")

# Абстрактна фабрика для транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass
    
    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

# Фабрика для Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")

# Оголошення змінних для фабрик
us_factory = USVehicleFactory()  # Оголошено фабрику США
eu_factory = EUVehicleFactory()  # Оголошено фабрику Європи

# Використання фабрик для створення транспортних засобів
vehicle1 = us_factory.create_car("Ford", "Mustang")  # Створюємо авто для США
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("BMW", "R1250GS")  # Створюємо мотоцикл для Європи
vehicle2.start_engine()

