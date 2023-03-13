
#reverse a number
num= 123
temp = num
rev = 0
while(num>0):
    r=num%10
    rev= rev*10+r
    num = num//10
print(f"reverse of a number: {rev}")

#palindrome
if(temp==rev):
    print("palimdrome")
else:
    print("not palindrome")    
        

