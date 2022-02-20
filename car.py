class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"走行距離は、{self.odometer_reading}kmです。")

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("走行距離は減らせません。")

    def increment_odometer(self, km):
        self.odometer_reading += km

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"この車のバッテリーは、{self.battery_size}kWhです。")

    def get_range(self):
        if self.battery_size == 75:
            range = 420
        elif self.battery_size == 100:
            range = 510

        print(f"この車の満充電時の航続距離は約{range}kmです。")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("この自動車にはガソリンのタンクはありません。")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()