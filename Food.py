import random

class Food:
    def __init__(self):
        self.x_coordinate = random.randint(1,140)
        self.y_coordinate = random.randint(1,9)
        type = random.randint(0,100)
        if type <=20:
            self.type_food = 0 #0= Bocadillo malo
        else:
            self.type_food = 1 #1= bocadillo bueno
        #señf.type_foof = random.randint(0,1)


    def print(self):
        print('x-coordinate: ',self.x_coordinate)
        print('y-coordinate: ', self.y_coordinate)
        print("bocadillo: ", self.type_food)


