class Cars():
    #CONSRUCTOR
    def __init__(self,manufactor,model,age,engine_format,cylinders):
        self.model = model
        self.age = age
        self.engine_format = engine_format
        self.cylinders = cylinders
        self.manufactor = manufactor
    def display(self):
        print(self.model)
        print(self.age)
        print(self.engine_format)
        print(self.cylinders)
        print(self.manufactor)
        

    

car1 = Cars("bmw","M4",3,"V",8)
car1.display()
car2 = Cars("Mercedes-Benz","AMG 1",4,"Hybrid, V",8)
car2.display()