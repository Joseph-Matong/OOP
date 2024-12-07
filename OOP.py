# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery_life = battery_life  # Encapsulated attribute

    def charge(self, hours):
        """
        Simulate charging the phone for a given number of hours.
        """
        self.__battery_life += hours * 10  # Each hour adds 10% charge
        if self.__battery_life > 100:
            self.__battery_life = 100
        print(f"{self.model} charged to {self.__battery_life}%.")

    def use(self, hours):
        """
        Simulate using the phone for a given number of hours.
        """
        battery_usage = hours * 15  # Each hour uses 15% charge
        if self.__battery_life - battery_usage < 0:
            print(f"{self.model} has run out of battery!")
            self.__battery_life = 0
        else:
            self.__battery_life -= battery_usage
            print(f"{self.model} battery is now at {self.__battery_life}%.")

    def get_battery_life(self):
        """
        Return the current battery life.
        """
        return self.__battery_life


# Derived class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def use(self, hours):
        """
        Overriding use() method to reduce battery usage for gaming phones.
        """
        battery_usage = hours * 10  # Gaming phone is more efficient
        if self.get_battery_life() - battery_usage < 0:
            print(f"{self.model} has run out of battery!")
        else:
            self._Smartphone__battery_life -= battery_usage
            print(f"{self.model} battery is now at {self.get_battery_life()}%.")


# Example Usage
iphone = Smartphone("Apple", "iPhone 14", "256GB", 100)
galaxy = GamingSmartphone("Samsung", "Galaxy S23 Ultra", "512GB", 100, "Advanced Cooling")

iphone.use(4)  # Normal smartphone
galaxy.use(4)  # Gaming smartphone with overridden behavior


# ACTIVITY 2

# Base class
class Vehicle:
    def move(self):
        pass  # Abstract method


# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")


# Example Usage
def demonstrate_movement(vehicle):
    """
    Demonstrate polymorphism by calling the move() method on different vehicle objects.
    """
    vehicle.move()


# Create objects
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Test polymorphism
for v in (car, plane, boat, bicycle):
    demonstrate_movement(v)
