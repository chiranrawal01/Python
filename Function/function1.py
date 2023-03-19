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

def sum (a,b):
    return a+b


def sub (a,b):
    return a-b


def mul (a,b):
    return a*b


def div (a,b):
    return a/b


#     print("Selection Operator")
#     print("Add")
#     print("Sub")
#     print("Mul")
#     print("Divide")

op = input("Enter operator to perform: ")


a =int(input("Enter a Number: "))
b=int(input("Enter b number: "))
if(op=="+"):
    print(f'sum is: {sum(a,b)}')
elif(op=='-'):
    print(f'sub is {sub(a,b)}')
elif(op=='*'):
    print(f'mul is {mul(a,b)}')  

elif(op=='/'):
    print(f'div is{div(a,b)}')          


   