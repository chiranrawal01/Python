'''def sum (a,b):
     return a+b
print("sum of numbers is:"+str(sum(2,4)))'''


'''#function to check if the number is even or odd.
def odd_even(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"
print(odd_even(9))    '''

'''#function to check prime number
def is_prime(num):
    if(num<2):
        return 'is prime'
    for i in range (2, num):
        if(num%i == 0):
            return "is not prime"
        
        return 'is prime'
    print(is_prime(9))'''

#Built a simple Calculator using Functions  (+, - ,*, /)

# def sum (a,b):
#     return a+b


# def sub (a,b):
#     return a-b


# def mul (a,b):
#     return a*b


# def div (a,b):
#     return a/b


# #     print("Selection Operator")
# #     print("Add")
# #     print("Sub")
# #     print("Mul")
# #     print("Divide")

# op = input("Enter operator to perform: ")


# a =int(input("Enter a Number: "))
# b=int(input("Enter b number: "))
# if(op=="+"):
#     print(f'sum is: {sum(a,b)}')
# elif(op=='-'):
#     print(f'sub is {sub(a,b)}')
# elif(op=='*'):
#     print(f'mul is {mul(a,b)}')  

# elif(op=='/'):
#     print(f'div is{div(a,b)}')          


'''
def std_info(name="xyz", section="B"):
    print(name)
    print(section)

std_info('asd','C')    '''

'''
#Create a function to add numbers
a =int(input("Enter a Number: "))
b=int(input("Enter b number: "))
c =int(input("Enter c Number: "))
d=int(input("Enter d number: "))
def sum (a,b,c,d):
    return a+b+c+d
op = input(" operator to perform: ")
if(op=="+"):
  print(f'sum is: {sum(a,b,c,d)}')   '''

'''def sum(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum) 

sum(1,2,3,4,5,6,7,8,9,10) '''   