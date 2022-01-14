class Car:
    # class attributes
    manufacturer = "GMC"
    number_of_cars = 0
    all_cars = []
    # init method / instance attributes
    def __init__(self, data):
        self.tank_size = data["tank_size"]
        self.gallons_of_gas = 0
        self.color = data["color"]
        self.year = data["year"]
        self.make = data["make"]
        self.model = data["model"]

        # updating class attribute values

        Car.number_of_cars += 1
        Car.all_cars.append(self)

    # class method
    @classmethod # decorator
    def total_gallons_of_gas(cls): # pass in 'cls' so class can be referenced
        total_gallons = 0
        for car in Car.all_cars:
            total_gallons += car.gallons_of_gas
        return total_gallons

    # static method
    @staticmethod # decorator
    def enough_gas(total_gas, gas_needed):
        if total_gas < gas_needed:
            print("Sorry! Not enough fuel")
            return False
        else:
            print("enjoy your trip!")
            return True

    # instance method
    def fill_tank(self): # pass in 'self'so individual instances can be referenced
        self.gallons_of_gas = self.tank_size

    def drive(self, miles):
        if Car.enough_gas(self.gallons_of_gas, miles):
            self.gallons_of_gas -= miles
        else:
            print("Looks like a stay at home day!")

    def get_car_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, and Tank Size: {self.tank_size}")
    

# data objects with instances of Car clas
subaru_data = {
    "tank_size": 18,
    "color": "Blue",
    "make": "Subaru",
    "model": "Crosstrek",
    "year": 2019,
}
subaru = Car(subaru_data)
# tacoma = Car(25, "Subaru", 2019)
civic_data = {
    "tank_size": 12,
    "color": "Silver",
    "make": "Honda",
    "model": "Civic",
    "year": 2006,
}
civic = Car(civic_data)
# Class Attributes / Method

# print(civic.manufacturer)
# print(subaru.manufacturer)
# print("================================")
# subaru.manufacturer = "Subaru"
# print(civic.manufacturer)
# print(subaru.manufacturer)
# print("================================")
# Car.manufacturer = "Honda"
# print(civic.manufacturer)
# print(subaru.manufacturer)
# print("================================")
# print(Car.number_of_cars)
# print(Car.all_cars)
# print("================================")
# subaru.fill_tank()
# civic.fill_tank()
# subaru.drive(5)
# print(Car.total_gallons_of_gas())

# Instance Attribute

# print(subaru.tank_size)
# print(tacoma.tank_size)
# print(civic.tank_size)

# print(subaru.color)
# print(tacoma.color)
# print(civic.color)

# subaru.color = "Red"
# print(subaru.color)
# Instance Method

# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# subaru.drive(5)
# print(subaru.tank_size)
# print("===============================")
# subaru.get_car_info()
# civic.get_car_info()
class Driver:
    def __init__(self, data):
        self.name = data["name"]
        self.age= data["age"]
        self.car = data["car"]

    def get_car_info(self):
        pass

driver1_data = {
    "name" : "Sbeve",
    "age" : 27,
    "car" : "Honda",
}
driver1_data = Driver(driver1_data)

driver2_data = {
    "name" : "Steve",
    "age" : 23,
    "car" : "Nissan",
}
driver2_data = Driver(driver2_data)

