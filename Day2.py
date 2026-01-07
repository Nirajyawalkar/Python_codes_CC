# <-----------------list---------------->

# A= (1,"ABC",2030)
# print(type(A))
# a = [4,3,1,2]
# print(a)
# print(a[1])
# print(a[-4])
# print(a[0:4])
# print(len(a))
# print(a[0:-1])
# a.append("Cherry")
# print(a)
# a.insert(0,"Mango")
# print(a)
# a.pop(2)
# print(a)
# a.clear()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.remove(3)
# print(a)
# del a it is a keyword used to delete an entire list
# print(a)
# b = [2,6,3,9,8,5]
# for i in range(0,5):
#     if(b[i]%2==0):
#         print("it is even no")
#     else:
#         print("it is not even no")


#<-----set ----->
# set1 = {"Apple","Orange","Mango"}
# set.add("cherry")
# print(set)
# set.update(["Chiku","Banana"])
# print(set)
# set.remove("Mango")
# print(set)
# set2 = {"Orange"}
# print(set1.union(set2))
# set1.clear()
# print(set1)
# del set1
# print(set1)
# set1.discard("Apple")
# print(set1)
# print(set1 & set2)
# print(set1 | set2)
# a = [i for i in  range(15)]
# print(a)

#<-----tuple------>

# a = (5,20,50,30,70,80)
# print(a)
# b =(10,20,30,50)
# c = a + b
# print(c)
# print(20 in a)# indentity operator
# print(30 is not 10)#membershp oprerator
# print(max(a))
# print(min(a))

##<----------------dictionary---------->
# dict  = {"Niraj": 25,"Vedant":60,"Om":27}
# print(dict)
# print(dict["Niraj"])
# print(dict.get("Om"))
# for key in dict:
#      print(key)
    # print(dict[key])
# print(len(dict))
# dict["age"] = 22 #adding the key and value in the dict
# print(dict)
# dict[0] = "string"
# print(dict)
# for value in dict.values():
#     print(value)
# # for key in dict():
# #     print(key)
# for key, value in dict.items():
#     print(f"{key}: {value}")
# del dict["Niraj"]
# print(dict)
# student = {
#     "name" = "john",
#     "age" = 20,
#     "grades": {
#         "math":85,
#         "science":90,
#         "english":78
#     }
#      "address": {
#          "street":"123 Main st",
#          "city":"Anytom",
#          "zip": "12345"
#      }
# }
# print("Name:",student["name"])
# print("Math grades:",student["grades"]["math"])
# print("City:",student["address"]["city"])\\
    
#<---------------functionas----------->

# def add(x,y):
#     z=x+y
#     return z
# a=add(2,3)
# print(a)
# def factorial(n):
#     fact = 1
#     i=0
#     while i!=n:
#         fact*=(n-i)
#         i+=1
#     print(fact)
# factorial(5)
# def add(x,y):
#     return(x+y)
# print("5+6=",add(5,6))
# print("10+16=",add(10,6))
def fruits(fruitlist):
    for name in fruitlist:
        print("I like ", name)
mylist = ["Mango","Orange","Apple"]
fruits(mylist)
