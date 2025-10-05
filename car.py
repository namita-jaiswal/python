class  Car:

    total_car = 0
    
    def __init__(self,brand,model):
       self.__brand = brand
       self.__model = model
       Car.total_car += 1 

    def get_brand(self):
        return self.__brand + "!"
    
# __ (double underscore) makes the attribute private

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self): # Polymorphism
        return "Petrol or Diesel"

    @staticmethod # decorators
    def general_def():
        return "Cars are cool!"
    
    @property
    def model(self):
        return self.__model

class  ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self): # Polymorphism
        return "Electric Charge"

my_car = Car("Toyota", "Corolla")
# # print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())

my_new_car = Car("Honda", "Civic")
# # print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name()) 

my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())
# print(my_tesla.fuel_type())
# print(isinstance(my_tesla, ElectricCar))
# print(isinstance(my_tesla, Car))

my_car_1 = Car("BMW", "X5")
# print(my_car_1.general_def ())
# print(Car.general_def)
 

my_car_2 = Car("Ford", "Mustang")
# print(my_car_2.fuel_type())
# print(Car.total_car)

# Overwriting
# my_car.model = "City"  # This will give error as model is read-only now
# print(my_car.model)

class Battery:
    def battery_info(self):
        return "This is a battery."


class Engine:
    def engine_info(self):
        return "This is an engine."


class ECar(Battery, Engine, Car):
    pass

my_tesla2 = ECar("Tesla", "Model s")
print(my_tesla2.battery_info())
print(my_tesla2.engine_info())