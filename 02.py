# z=int(input("enter the value of z: "))
# if(z>0):
#     print("its positive")20
# elif(z<0):
#     print("its negative")
# else:
#     print("zero")

    
  
    
    #find the area of a triangle given 3 sides (a,b,c)


# import math
# a = 20
# b= 10
# c=20

# sum=(a+b+c)/3
# print("sum : "+str(sum)) 
# area=(math.sqrt(sum*(sum-a)*(sum-b)*(sum-c)))
# print("area: "+str(area))


#find the area of circle
# import math
# r=int(input("enter the value:"))
# pi=3.14
# A = pi*r*r
# print("A: "+str(A))


#solve quadratic equation
import math
a=int(input("enter the value a: "))
b=int(input("enter the value b: "))
c= int(input("enter the value c: "))
eqn = b**2-(4*a*c)
if(eqn<0):
    print("Imaginary Roots:")  
else:
    eqn2=(-b+(math.sqrt(eqn)))/2*a
    eqn3 = (-b-(math.sqrt(eqn)))/2*a
    print(f"Roots: {eqn2:.2f}, {eqn3:.2f}")    



    