#Lists
# Similar Data Type Store....

somelist = [1,2,3,4,5,6,7,8,9,10]
for x in somelist:
    print(x)


thislist=list(("apple","banana","Cheery"))
for x in thislist:
    print(x)

    #lists
    somelist = [1,2,3,4,5,6,7,8]
    random_list = ["hello", "world","hello", "world", ]
    for ind, x in enumerate(random_list):
        print(ind,x)


        # Mutable // Chnageable
        # mmutable // Not changeable
        
somelist = [1,2,3,4,5,6,7,8]
random_list = ["hello", "world","hello", "world", ]
for ind, x in enumerate(somelist):
    if(x==5):
        somelist[ind]=100
    print(ind,x)
for x in somelist:
    print(x)    
