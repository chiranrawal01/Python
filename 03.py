#find the smallest numbers betwwen 3 numbers.
import math
a= int(input("enter the value of a: "))
b= int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

if(a<b):
    if(a<c):
        print("A is Smallest : ")
    else:
            if(b<c):
               print("b is smallest")

else:
    print("smallest c.")                    