#Find sum of numbers untill zero or negative number is enterned.
a= int(input("enter the number:"))
b= int(input("enter the number: "))
sum=a+b
while(a>0):
    a= int(input("enter the number:"))
    sum+=a

print(f"sum of number: {sum}")
