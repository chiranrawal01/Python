# smallest num frtom list

# a = [24,34,3,4,45,67]
# smallest = a[0]
# for i in a:
# 	if i<smallest:
# 		smallest = i	
# print("smallest number is :", smallest)

# sum of even and odd from list
a =[24,34,3,4,45,67]
even =0
odd =0
for i in range(6):
    if (a[i]%2 == 0):
        even+=a[i]
for i in range(6):
    if (a[i]%2 != 0):
        odd+=a[i]
print (f"The Sum of even is: {even}")
print (f"The Sum of odd is: {odd}")




