# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
#     def get_balance(self):
#         return self._balance
#     def deposit(self,amount):
#         self._balance += amount
# account = BankAccount(1000)
# print(account.get_balance())
# account.deposit(200)
# print(account.get_balance())

# class Deposit:
#     def __init__(self, amount):
#         self.__amount = amount

#     def get_amount(self):
#         return self.__amount

# class Bank:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance
#         self.__deposits = []

#     def deposit(self, deposit_obj):
#         if deposit_obj.get_amount() > 0:
#             self.__deposits.append(deposit_obj)
#             self.__balance += deposit_obj.get_amount()

#     def get_balance(self):
#         return self.__balance

# acc = Bank(1000)
# print(acc.get_balance())  # 1000

# acc.deposit(Deposit(200))
# print(acc.get_balance())  # 1200

#<<<<<<<<<<<<polymophism>>>>>>>>>
# class Animal:
#     def sound(self):
#         return "Some sounds of animal"
# class cat(Animal):
#         def sound(self):
#             return "Meow Meow"
# class dog(Animal):
#     def sound(self):
#         return "Bark Bark"
# animals = [dog(), cat(), Animal()]
# for animal in animals:
#     print(animal.sound())
    
#<<<<<<<<<<<<<<<<< abstraction >>>>>>>>>>>>>>>>>>>>>>
# from abc import ABC , abstractmethod
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     @abstractmethod
#     def printdetails(self):
#             pass
#     def accelerate(self):
#         print("speed up")
    
#     def break_applied(self):
#         print("Car stopped")
        
# class Hatchback(Car):
#     def printdetails(self):
#         print("Brand: ",self.brand)
#         print("Model:  ",self.model)
#         print("Year: ",self.year)
    
#     def sunroof(self):
#         print("Not available")

# class Suv(Car):
#     def printdetails(self):
#         print("Brand: ",self.brand)
#         print("Model:  ",self.model)
#         print("Year: ",self.year)
    
#     def sunroof(self):
#         print("Available")
# car1 = Hatchback("maruti","alto",)

# car1.printdetails()
# car1.accelerate()
# car1.sunroof()

#<<<<<<<<<<<stack>>>>>>>>>>>>........

# stack = []
# #push
# stack.append("A")
# stack.append("B")
# stack.append("C")
# print("Stack: ", stack)

# #peek
# topElement = stack[-1]
# print("Peek: ",topElement)

# #pop
# PoppedElements = stack.pop()
# print("Pop: ",PoppedElements)

# #stack After Pop
# print("Stack After Pop: ",stack)

# #isempty
# isempty = not bool(stack)
# print("isempty: ",isempty)

########<<<<<<<<<<<#####linked list#####>>>>>>>>>>>>>>###########

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
        
    def push(self,value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
    def pop(self):
        if self.isempty():
            return "stack is empty"
        Popped_node = self.head
        self.head = self.head.next
        self.size -=  1
        
    def peek(self):
        if self.isempty():
            return "Stack is empty"
        return self.head.value
    
    def isempty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
    
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value,end=" -> ")
            currentNode = currentNode.next
            print()
            
            
myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("Linkedlist: ",end="")
myStack.traverseAndPrint()
print("push ",myStack.push())
print("pop: ",myStack.pop())
print("Linkedlist after pop:",end="")
myStack.traverseAndPrint()
print("isEmpty:",myStack.isempty())
print("Size:",myStack.stackSize())


    
        
    

