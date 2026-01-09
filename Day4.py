# dict  = {"Niraj": 25, "om": 30, "pritam": 57}
# dict1 = {"place": "Nagpur", "store": "prada", "hometown": "chandrapur"}
# mydict = dict.update(dict1)
# print(dict)

# list = [10,20,30,40]
# def secondlargest(list):
#     max=secmax=0
#     for i in list:
#         if i>max:
#             max=i
#     for i in list:
#         if i>secmax and i<max:
#             secmax=i
#     return secmax
# print(secondlargest(list))
# print(sorted(dict))

# l = [1,2,3]
# set = {1,2,3,1,4}
# p = list(set)

# def duplicate(p,l):
#     count=0
#     for i in p:
#         if i in l:
#             l.remove(i)
# print(l)

# <----------oops---------->

# class Name:
    

#     def __init__(self, name, age):
#         self.name = name  
#         self.age = age  


# name = Name("Niraj", 19)

# print(name.name) 
# print(name.age)


# class student:
#     def __init__(self,name,roll):
#         print(name)
#         print(roll)
# s1=student("Niraj",100)#constructor with parameterized

# class student:
#     def __init__(self):
#         print("hi")
#     def Info(self):
#         print("Niraj")
#         print("20")
# s1=student()
# s1.Info()# it is without  parameter

#<-------single inheritance--------->
# class Rectangle:
#     def rec_area(self,height,width):
#         area = height*width
#         print(area)
# class Square(Rectangle):
#     def squ_area(self,side):
#      area = side*side
#      print(area)
# obj=Square()
# obj.rec_area(10,20)
# obj.squ_area(10)

#<<<<<<<<<<<<<< multiple>>>>>>>>>>>>>>>>>>..
# class Square:
#     def sq_area(self,side):
#      area = side * side
#      print(area)
# class triangle:
#     def tri_area(self,base,height):
#         area = 0.5 * base * height
#         print(area)
# class rectangle(Square,triangle):
#     def rec_area(self,height,width):
#         area = height * width
#         print(area)
# area1 =rectangle()
# area1.sq_area(4)
# area1.tri_area(15,20)
# area1.rec_area(20,30)

#<<<<<<<<<<<<< hireachical >>>>>>>>>>>>>.

# class rectangle:
#     def rec(self,height,width):
#         area = height * width
#         print(area)
# class triangle(rectangle):
#     def tri(self,height,base):
#         area  = height * base
#         print(area)
# class Square(rectangle):
#     def squ(self,side):
#         area = side * side
#         print(area)
# area2 = Square()
# area2.rec(25,30)
# area2.squ(40)
# area3 = triangle() # type: ignore
# area3.tri(56,30)

#<<<<<<<<<<<<<< multilevel >>>>>>>>>>>>>>>>>>>>>
# class square:
#     def squ(self,side):
#         area  =  side *  side
#         print(area)
# class rectangle(square):
#     def rec(self,height,width):
#         area  = height * width
#         print(area)
# class triangle(rectangle):
#     def tri(self,height,base):
#         area = 0.5 * height * base
#         print(area)
# area1 =triangle()
# area1.squ(4)
# area1.tri(15,20)
# area1.rec(20,30)

    
#<<<<<<<<<<<<< hybird >>>>>>>>>>>> 
 
# class square:
#     def squ(self,side):
#         area  =  side *  side
#         print(area)
# class rectangle:
#     def rec(self,height,width):
#         area  = height * width
#         print(area)
# class triangle(rectangle,square):
#     def tri(self,height,base):
#         area = 0.5 * height * base
#         print(area)
# class circle(triangle):
#     def cir(self,radius):
#         area  = 3.14  * radius * radius
#         print(area)
# area1 = circle()
# area1.squ(4)
# area1.tri(15,20)
# area1.rec(20,30)
# area1.cir(25)


#<<<<<<<<<<< vechicle class >>>>>>>>>.

# class vechicle:
#     def eng(self):
#         print("It is engine of Vechile")
# class Brand(vechicle):
#     def brn(self):
#         print("it is bmw brand")
# class logo(vechicle):
#     def log(self):
#         print("logo of bmw motorworks")
# c1 = logo()
# c1.eng()
# c1.log()
# c2 = Brand()
# c2.brn()
#<<<<<<< encapsulation >>>>>>>>>>>>

# class Public:
#     def __init__(self):
#         self.name = "Niraj"
#     def display_name(self):
#         print(self.name)
# obj = Public()
# obj.display_name()
# print(obj.name)

# class Private:
#     def __init__(self):
#         self._age = 63
# class Subclass():
#     def display_age(self):
#         print(self._age)
# Obj = Private()
# Obj.display_age()

# a = "12345"
# b = int(a)
# print(b+2)

#<<<<<<<<< bank account >>>>>>>>>>>>>>..

# class bank:
#     def __init__(self):
        
        
