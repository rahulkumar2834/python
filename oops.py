# class Factory:
#     a=12 #attribute

#     def hello(self): #method
#         print("how are you")

#     print("hello how are you i am getting initialized")
# print(Factory().a)
# Factory().hello()






# class factory:
#     def __init__(self,material,zip,pockets):
#         self.material=material
#         self.zip=zip
#         self.pocket=pockets

#     def show(self):
#         print(f"your object details are {self.material},{self.zip},{self.pocket}")

    
# reebok = factory("leather",3,2)

# campus = factory("nylon",3,3)

# reebok.show()









# class animal:
#     name="tiger"

#     def __init__(self,age):
#         self.age=age

#     def show():
#         print(f"how are you your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print(f"how are you brother")

#     @staticmethod
#     def ststic():
#         print(f"how are you")







# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"hello your name is {self.name}")

# class human(Animal):
#     pass


# animal1=Animal("lion")
# persion1=human("rahul")

# persion1.show()





# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"this ia a  {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
    
#     def show(self):
#         print(f"hello your name is {self.name} age {self.age}")

# animal1=Animal("lion")

# human1=Human("rahul",21)

# animal1.show()
# human1.show()





# material
# zips
# colour
        
# class Factory:
#     def __init__(self,material):
#         self.material=material
#     def show(self):
#         print(f" your material is {self.material}")
    

# class BhopalFactory(Factory):
#     def __init__(self, material,zips):
#         super().__init__(material)
#         self.zips=zips
#     def show(self):
#          print(f"your material {self.material},numbers of zips are {self.zips}")

# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips,colour):
#         super().__init__(material, zips)
#         self.colour=colour
#     def show(self):
#          print(f"your matrial is {self.material},number of zips is {self.zips},and colour is {self.colour}")

# factory1=Factory("leather")
# factory2=BhopalFactory("cotton",2)
# factory3=PuneFactory("rubber",3,"red")

# factory3.show()
# factory2.show()
# factory1.show()