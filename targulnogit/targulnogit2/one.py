
class Dog():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if type(value) == int:
            self._age  = value

    def __str__(self):
        return f" {self._name}  is {self._age} years old"
    
    def cleandog(self):
        return f"the price for cleaning {self._name} is 20 dollars  "

rax = Dog("rax " ,3)
print(rax.name)
rax.name = "maaa"
rax.age =13
print(rax.age)
rax.name = "flafi"
print(rax)
print(rax.cleandog())





