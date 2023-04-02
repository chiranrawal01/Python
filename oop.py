# # inheritence
# class person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def some_function(self):
#         print('Hello from parent.')

#     def welcome(self):
#         print(f"welcome {self.fname} {self.lname}.")


# class student(person):
#     def __init__(self, fname, lname, course):
#         super().__init__(fname, lname)
#         self.course = course

#     def child_function(self):
#         print('Hello from child class')

#     def welcome(self):
#         print(f"Welcome {self.fname} {self.lname} to {self.course}")  

# child_obj = student('xyz' , 'abc', 'c programming')
# child_obj.welcome ()               


# op in python
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return (f'Hello, I am {self.name} and I am {self.age}')
    def get_name(self):
        return f"Hi My Name is {self.name}"
    
    def get_age(self):
        return f"My age is (self.age)"    

p_obj = person('Chiran', 21)
print(p_obj)    