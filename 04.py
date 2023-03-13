# Print Even Number From 1 to 30 ?

# a = int (input("Enter A Num :"))
# b= int(input("Enter B Num :"))
# i=0
# while(i<10):
#     print(i)
#     i+= 1

# i=0
# while(i<=30):
#   if(i%2==0):
#     print(i)
#   i+= 1

#simple calculator
print("operations: ")
print("Addition: +")
print("Substraction: -")
print("Division: /")
print("Percentage: %")
print("-----------")

opt = 'y'
while(opt=='y'):
    ope = input("enter operation: ")
    op1 = int(input("enter operand 1: "))
    op2 = int(input("enter operand 2: "))

# Indentation
    if(ope == "+"):
        print(f"sum of{op1} and {op2} is {op1 + op2}")
    elif(ope == "-"):
        print(F"sub of {op1} and {op2} is {op1 - op2}")
    elif(ope == "*"):
        print(f"mul of {op1} and {op2} is {op1 * op2}")
    elif(ope == "/"):
        print(f"div of {op1} and {op2} is {op1 / op2}")
    elif(ope== "%"):
        print(f"per of {op1} and {op2} is {(op1 % op2)/100}")
    else:
       print("invalid operations.")

    opt = input("do you want try again (y/n): ")
