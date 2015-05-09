import pygame
import random
import numpy as np
from Species_And_GameWorlds import*

# Hunt! Mate! Discover! Feed thyself!

class Organism:

    DNA=[]
    
    def __init__(self, pioneer,LocationX,LocationY,parent,Type):

        self.Type=Type
        
        if pioneer==True:
            # intelligence, fitness, partners, mating probability,size,vision
            self.Color = Species[Type]["Color"]
            self.Intelligence=Species[Type]["Intelligence"]
            self.Fitness=Species[Type]["Fitness"]
            self.Max=Species[Type]["Max"]
            self.Partners=Species[Type]["Partners"]
            self.Mating=Species[Type]["Mating"]
            self.Size=Species[Type]["Size"]
            self.Age=Species[Type]["Age"]
            self.MaxAge=Species[Type]["MaxAge"]
            self.Vision=Species[Type]["Vision"]
            ##Not a shred of intelligence, blind as bats


        if pioneer==False:
            # intelligence, fitness, partners, mating probability,size,vision
            self.Color = Species[Type]["Color"]
            self.Intelligence=parent.Intelligence+(random.uniform(-1, 1)*random.random()/10)
            self.Fitness=parent.Max
            self.Max=self.Fitness+random.randint(-5,+5)
            self.Partners=parent.Partners
            if random.random()<0.2:
                self.Partners=1-parent.Partners

            if self.Partners==0:
                self.Color = (abs(255-self.Color[0]), abs(255-self.Color[1]), self.Color[2])
            
            self.Mating=parent.Mating+(random.uniform(-1, 1)*random.random()/100)
            self.Size=parent.Size+(random.uniform(-1, 1)*random.randint(0,1))
            if self.Size<2:
                self.Size=2
                
            self.Vision=parent.Vision+(random.uniform(-1, 1)*random.randint(0,1))
            self.Age=parent.MaxAge
            self.MaxAge=self.Age+random.randint(-5,+5)
            
            
            
            
        self.Location=[LocationX,LocationY]



    def Update(self,Predators, Friend_Locations, Food_Locations):

        Closest=-1
        if len(Food_Locations)>0 and random.random()<self.Intelligence:
           nodes = np.asarray(Food_Locations)
           point=(self.Location[0],self.Location[1])
           dist_2 = np.sum((nodes - point)**2, axis=1)
           Closest=np.argmin(dist_2)
           movex=Food_Locations[Closest][0]-self.Location[0]
           movex= np.sign(movex)
           movey=Food_Locations[Closest][1]-self.Location[1]
           movey= np.sign(movey)


        elif len(Predators)>0 and random.random()<self.Intelligence:
            nodes1 = np.asarray(Predators)
            point1=(self.Location[0],self.Location[1])
            dist_3 = np.sum((nodes1 - point1)**2, axis=1)
            Closest=np.argmin(dist_3)
            movex=Predators[Closest][0]-self.Location[0]
            movex= -1*np.sign(movex)
            movey=Predators[Closest][1]-self.Location[1]
            movey= -1*np.sign(movey)



        elif len(Friend_Locations)>0 and self.Partners==1 and random.random()<self.Intelligence:
            nodes1 = np.asarray(Friend_Locations)
            point1=(self.Location[0],self.Location[1])
            dist_3 = np.sum((nodes1 - point1)**2, axis=1)
            Closest=np.argmin(dist_3)
            movex=Friend_Locations[Closest][0]-self.Location[0]
            movex= np.sign(movex)
            movey=Friend_Locations[Closest][1]-self.Location[1]
            movey= np.sign(movey)
          
        else:
            movex=random.randint(-1,1)
            movey=random.randint(-1,1)


        self.Location[0]=self.Location[0]+movex
        self.Location[1]=self.Location[1]+movey


        


        

      
            
        
                 
        
            
        

        



        
        
        

        self.Fitness=self.Fitness-0.5
        self.Age=self.Fitness-0.1
        
        
        
        

        
