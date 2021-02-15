
class person(object):
    population = 50
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age>=18
    
    def display(self):
        print(self.name,'is',self.age,'years old.')
        
newPerson = person('Aakash',20)
# class method => can be called with the help of the class or 
# methods which doesn't need any objects for it
print(person.getPopulation())

# static methods = > similar to classmethod but it doesn't need to class object and
#  self{which doesn't need any thing to be done with class variables}
print(person.isAdult(5))