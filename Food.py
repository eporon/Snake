import random

class Food:
    def __init__(self):
        self.x_coordinate = random.randint(1,80)
        self.y_coordinate = random.randint(1,25)
        type = random.randint(0,100)
        if type <=20:
            self.type_food = 0 #0= Bocadillo malo
        else:
            self.type_food = 1 #1= bocadillo bueno
        #señf.type_foof = random.randint(0,1)
