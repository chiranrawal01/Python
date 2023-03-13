# insert Data ti thwe list.
some_List = [1,2,3,4,5]

some_List.append(6)  #element add
print(some_List)

some_List.insert(2,7)  # first value ko paxadi asign garyako value aauxa
print(some_List) 


e_List = []

for i in range(0,51):
    if(i%2==0):
        e_List.append(i+1)
    else:
        e_List.append(i-1)
print(e_List)