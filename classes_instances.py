#working with classes and instances
class Car:
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    my_new_car = Car('audi', 'a7', 2026)
    print(my_new_car.get_descriptive_name())

    



