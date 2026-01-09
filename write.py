# fileptr = open("a.txt","w")
# fileptr.write("Hello")
# fileptr.close()

# fileptr = open("a.txt","r")
# fileptr.write("Hello")
# fileptr.close()

# fileptr = open("a.txt","a")
# fileptr.write("\n Hello i am niraj" )
# fileptr.close()


fileptr = open("a.txt","r")
a = fileptr.read()
print(a)
fileptr.close()
