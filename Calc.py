
# a=int(input("Enter A Number : "))
# b = int (input("Enter B Number :"))

# sum = a+b
# Diff = a-b
# Mul = a*b
# Div = a/b
# Mod = a%b

# print(f"The Sum is :{sum}")
# print(f"diff: {Diff}")

#simple calculator
print("operations: ")
print("Addition: +")
print("Substraction: -")
print("Division: /")
print("Percentage: %")
print("-----------")

ope = input("enter operation: ")
op1 = int(input("enter operand 1: "))
op2 = int(input("enter operand 2: "))

if(ope == "+"):
    print(f"sum of{op1} and {op2} is {op1 + op2}")
elif(ope == "-"):
    print(F"sub of {op1} and {op2} is {op1 - op2}")
elif(ope == "*"):
    print(f"mul of {op1} and {op2} is {op1 * op2}")
elif(ope == "/"):
    print(f"div of {op1} and {op2} is {op1 / op2}")
elif(ope== "%"):
    print(f"per of {op1} and {op2} is {op1 % op2}")
else:
     print("invalid operations.")
