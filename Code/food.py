import pygame
import random
from AwesomeToolkit import *

# Feed thyself!

class Food:

    DNA=[]
    Type="Samiran"
    def __init__(self,LocationX,LocationY):
        self.Location=[LocationX,LocationY]
        self.Energy=random.randint(10,20)
        self.Fitness=100
        self.Color = (255, 200, 200)



    def Update(self):
        
        # Hunt! Mate! Discover! Feed thyself!
        
        
        

        self.Fitness=self.Fitness-0.1
        
        
