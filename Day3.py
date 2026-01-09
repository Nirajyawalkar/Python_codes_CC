#<------------string-------------------->
#  print(Str)
# print(Str[0:5])

# Str = """I am leraning python 
# and it is very easy to 
# understand """
# print(Str)
# for i in Str:
#     print(i)
# print(len(Str))
# print(Str[0:57])
# print(str.upper())#it is used to convert the into lowercase
# print(str.lower())#it is used to convert the into uppercase
# print(str.capitalize())#it is used the captial the first letter
# print(str.casefold())#it is used small the first letter
# print(str.center(60))# it is used to center the ouput in the terminal 
# print(str.endswith("n"))
# print(str.startswith("P"))
# x = int(input("enter the no : ")) 
# print(str[::-1])
# print(str.split())# it is used to split the string


#<--------------.format operator for concatenation of string------------>

# str =  "hogward"
# str1 = "500"
# print("{} the pric is {} ".format(str,str1))
# str = "assasasnin"
# print((str+" ")*100)#for printing the n no times a specfic n

#<------------exception handling-------------->

# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.

# try:
#     a=10
#     b=2
#     c=a/b
#     print(c)
# except:
#     print("Error")
# else:
#     print("Error")
# finally:
#     print("finally")

# s = input("Enter the String : ")
# w=0
# c=0
# for i in (0,len(s)-1):
#     if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
#         print("its is vowel")
#         w+=1
#     else:
#         print("It is not ")
#         c+=1
#         print(w)

list = [1,3,2,4]
# list.sort()
# print(list)
a  = tuple(list)
print(a)

#<-------------file handling ---------------->
