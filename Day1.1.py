# # '''x = int(input("enter the no1 : "))
# # y = int(input("enter the no2 : "))
# # if(x<y):
# #     print("%d is less than %d"%(x,y))
# # elif(x>y):
# #     print("%d is greater than %d"%(x,y))
# # else:
# #     print("%d is equal to %d"%(x,y))
# # for i in range(1,10):
# #     print(i)
# # '''

# # #<-------even or odd------>
# # x = int(input("Enter the no1 : "))
# # if (x%2 == 0):
# #     print("%d is even "%x)
# # else:
# #     print("%d is odd "%x)
# #     
    
#     #<-----+ve,-ve, or zero----->
# # '''x = int(input("Enter the no1 : "))
# # if(x<0):
# #     print("%d is -ve "%x)
# # if(x>0):
# #     print("%d is +ve "%x)
# # if(x==0):
# #     print("%d is equal to zero"%x)
# #     '''
    
# # '''#<-----voting sysytem---->
# # x = int(input("Enter the no1 : "))
# # if(x>=18):
# #     print("it is eligible for vote")
# # else:
# #     print("it is not eligible for vote")
# # '''
# # x = int(input("Enter the no1 : "))
# # if(x>=90):
# #     print("%d is in Class A"%x)
# # elif(x>=60 and x<90):
# #     print("%d is in Class B"%x)
# # elif(x>=35 and x<60):
# #     print("%d is in Class C"%x)
# # else:
# #     print("%d is in a fail semester"%x)

#      #<------simple intrest ------------>
# # x = float(input("Enter the principle : "))
# # y = float(input("Enter the rate : "))
# # z = float(input("Enter the time : "))
# # s = x * y * z / 100
# # print(s)

#<----looping statement--->
# # for i in range(0,100,2):
# #     print(i)
# s = "niraj"
# for i in input(s):
#     print(i)

#<---table of any number---->

# num = int(input("Enter the no : "))
# for i in range(1,11):
#     print(num*i)
# i = 1
# num = int(input("Enter the no : "))
# while(i<=10):
#     print(num*i)
#     i=i+1

# str = "Niraj"
# i=0
# while i <len(str):
#     print(str[i])
#     i=i+1

# for x in range(1,11):
#     if x==5:
#         continue
#     else:
#         print(x)
# for x in range(1,11):
#     if x==5:
#         break
#     else:
#         print(x)       
# x=5
# if(x>2):
#     if(x>3):
#         print("A")
        
#<-----logical and relational------->

# x = float(input("Enter the no1 : "))
# y = float(input("Enter the no2 : "))
# z = float(input("Enter the no3 : "))
# if x>y and x>z:
#     print(x,"is greatest")
# if y>x and y>z:
#     print(y,"is greatest")
# if z>x and z>y:
#     print(z,"is greatest")

#Assingment opertator
# x1 = 9
# y1 = 4
# x1 += y1
# print(x1)
# x2 = 9
# y2 = 4
# x2 -= y2
# print(x2)
# x3 = 9
# y3 = 4
# x3 *= y3
# print(x3)
# x4 = 9
# y4 = 4
# x4 /= y4
# print(x4)
# x5 = 9
# y5 = 4
# x5 **= y4
# print(x4)
# x6 = 9
# y6 = 4
# x6 %= y6
# print(x6) 

#<----bitwise operator---->
# x = 6
# y = 3
# print("x&y=",x&y)
# print("x|y=",x|y)
# print("x>>2=",x>>2)
# print("x<<2=",x<<2)
# print("x^y=",x^y)
