# 
x = 4
s_list = [1,2,3,4,5,6]
try :
    print(s_list[7])
except ZeroDivisionError:
    print('ZeroDivisionError')
except IndexError:
    print('index error')


else:
    print('No error')
finally :
    print('This is a Final block')