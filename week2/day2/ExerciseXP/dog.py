#Instructions:
#Step 1: Create the Dog Class
#Create a class called Dog with name, age, and weight attributes.
#Implement a bark() method that returns “<dog_name> is barking”.
#Implement a run_speed() method that returns weight / age * 10.
#Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.
#Step 2: Create Dog Instances
#Create three instances of the Dog class with different names, ages, and weights.
#Step 3: Test Dog Methods
#Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

class Dog():
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    def get_name(self):
        return self.__name
    def bark(self): 
        return f'{self.__name} is barking'
    def run_speed(self):
        return self.__weight / self.__age * 10
    def fight(self, other_dog):
        if self.run_speed() * self.__weight > other_dog.run_speed() * other_dog.__weight:
            return f'{self.__name} wins the fight against {other_dog.__name}'
        else:
            return f'{other_dog.__name} wins the fight against {self.__name}'

if __name__ == "__main__":    
    dog1 = Dog("Rex", 4, 20)
    dog2 = Dog("Max", 5, 25)
    dog3 = Dog("Buddy", 3, 15)
    print(dog1.fight(dog2))
    print(dog3.run_speed())
    print(dog2.bark())
