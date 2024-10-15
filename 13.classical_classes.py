"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

class Person: #Person Class and has attributes of name and age
  species = 'homosapien'

def __init__ (self, name, age):
    self.name = name
    self.age = age

Bob = Person()

Bob = Person("Bob", 15)
print("random.name")
print("random.age")



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def introduce(self):
        print("This animal's name is " + self.name +". They are " + str(self.age) + " years old.")
#Subclasses of the Animal class
class Dog(Animal):
    def speak(self):
        print("Bark, Woof!")

class Cat(Animal):
    
    def speak(self):
        print("Meow, Hsss!")

#Executes functions in Animal, Dog, and Cat classes
ginger= Cat("Ginger", 3)
ginger.introduce()
ginger.speak()
Katie = Dog("Katie", 5)
Katie.introduce()
Katie.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount: #Bank Account Class
   class BankAccount:
    def __init__(self, owner, balance = 2000):
        self.owner = owner
        self.balance = balance

    def widthdraw(self, widthdrawl):
        self.widthdrawl = widthdrawl
        self.balance = self.balance - self.widthdrawl

    def deposit(self, depositing):
        self.depositing = depositing
        self.balance = self.balance + self.depositing

nathan = BankAccount("Nathan")
nathan.widthdraw(20)
print(nathan.balance)
nathan.deposit(50)
print(nathan.balance)