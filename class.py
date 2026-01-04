#creating and using a class
class dog:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(F'{self.name} is now sitting.')
    def roll_over(self):
        print(F'{self.name} is rolled over!')

class dog:
    my_dog = dog('browny', 5)
    print(f'my dog name is {my_dog.name}.')
    print(f'my dog is {my_dog.age} years old.')

        
