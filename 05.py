#collatz conjecture
#sum of even numbers, odd numbers up to 1000

# num=int(input("enter num: "))
# step=0


# while(num != 1):
#     if(num%2==0):
#         num=num//2
        
#     else:
#         num = num*3 + 1    
#     step+= 1    

# print(f"number of step: {step}")

# find the sum of even1 num amd odd num upto 1000

num=1
even=0
odd=0
while(num <=1000):
    if(num%2==0):
        even+=num
    else:
        odd+=num
    num+=1    

print(f"the sum of the even: {even}") 
print(f"the sum of the odd: {odd}")  
