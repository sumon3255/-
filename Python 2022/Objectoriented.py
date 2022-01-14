#OOP in Python
# name =  "jhon"
# age = 34
# print(name,age)

# class Person:
#     def print_details(self):
#         return self.name ,self.age

# p1 = Person()
# p2 =  Person()
# p1.name = "Jhon"
# p1.age = 34
# p2.name = "Michel"
# p2.age = 34
# print(p2.name)
# print(p2.age)



class Employee:
    __name = None
    __age = 0
    __salary = 0
    
    def __init__(self,fname,fage):
        self.name = fname
        self.age = fage
        
        
    
    # def set_name(self,name):
    #     self.__name = name
    
    # def get_name(self):
    #     return self.__name
    
    # def set_age(self,age):
    #         self.__age= age
    
    # def get_age(self):
    #     return self.__age
        
    
       
    

p1 = Employee("Jhon",34)
print(p1.name)
print(p1.age)
# p1.set_name("Jhon")
# p1.set_age(34)
# print(p1.get_name())
# print(p1.get_age())
    
   



        