import pygame
import OrganismClass
import GameWorld
import random
import food
import time
import pickle
import numpy as np

pygame.init()
pygame.display.set_caption('Data Collection')
screen = pygame.display.set_mode((600,600))
done = False



myfont = pygame.font.SysFont("monospace", 15)

# render text

TIME={}

  

clock = pygame.time.Clock()

go=1

Temp=[]
Temp1=[]
Temp2=[]
Temp3=[]
Temp4=[]

TempS=[]
Temp1S=[]
Temp2S=[]
Temp3S=[]
Temp4S=[]
IntelligenceGraph=[]
def Iteration(Organisms,Foods,Step):
    start = time.time()
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go=0

    


    ONumber=len(Organisms)
    FNumber=len(Foods)
    Temp=[]
    Temp1=[]
    Temp2=[]
    Temp3=[]
    Temp4=[]
    
    for i in Organisms:
        Temp.append(i.Intelligence)
        Temp1.append(i.Vision)
        Temp2.append(i.Max)
        Temp3.append(i.Age)
        Temp4.append(i.Mating)
    try:
        AvgInt=sum(Temp)/len(Temp)
        AvgVision=sum(Temp1)/len(Temp1)
        AvgMax=sum(Temp2)/len(Temp2)
        AvgAge=sum(Temp3)/len(Temp3)
        AvgMating=sum(Temp4)/len(Temp4)
    except ZeroDivisionError:
        AvgInt=0
        AvgVision=0
        AvgMax=0
        AvgAge=0
        AvgMating=0
    TempS.append(AvgInt)
    Temp1S.append(AvgVision)
    Temp2S.append(AvgMax)
    Temp3S.append(AvgAge)
    Temp4S.append(AvgMating)

    




    Toshow="Organisms: "+str(ONumber)+" Food Pellets: "+str(FNumber)+" Average Intelligence: "+str(round(AvgInt,5))
    label = myfont.render(Toshow, 1, (205,205,0))
    screen.blit(label, (10, 10))

    Toshow="Steps: "+str(Step)
    label = myfont.render(Toshow, 1, (205,205,0))
    screen.blit(label, (10, 30))


    
    

    
    if len(Foods)<300:
        for i in range(3):
            Foods.append(food.Food(random.randint(10,590),random.randint(10,590)))
    
  
    
    
    for organism in Organisms:

        Food_Locations=[]
        Friend_Locations=[]
        Predators=[]
      

        for pellet in Foods:
            if (abs(pellet.Location[0]-organism.Location[0])<=organism.Vision):
                if (abs(pellet.Location[1]-organism.Location[1])<=organism.Vision):
                    Food_Locations.append([pellet.Location[0],pellet.Location[1]])

        for organismz in Organisms:
            if organismz.Type!=organism.Type and organismz.Size<organism.Size:
                Food_Locations.append([organismz.Location[0],organismz.Location[1]])


        for organismx in Organisms:
            if organismx!=organism:
                if (abs(organismx.Location[0]-organism.Location[0])<=organism.Vision):
                    if (abs(organismx.Location[1]-organism.Location[1])<=organism.Vision):
                        if organismx.Type==organism.Type:
                             Friend_Locations.append([organismx.Location[0],organismx.Location[1]])
                        else:
                            Predators.append([organismx.Location[0],organismx.Location[1]])
                           

        try:
            organism.Update(Predators,Friend_Locations,Food_Locations)
        except NameError:
            pass





        
        
        pygame.draw.rect(screen, organism.Color, pygame.Rect(organism.Location[0], organism.Location[1], organism.Size, organism.Size))
        if (random.random()<=organism.Mating) and (organism.Partners==0):
            Organisms.append(OrganismClass.Organism(False,organism.Location[0],organism.Location[1],organism,organism.Type))



        for organism2 in Organisms:
            if organism2!=organism and organism.Partners==1 and organism2.Partners==1 and organism.Type==organism2.Type and organism2.Location[0]==organism.Location[0] and pellet.Location[1]==organism.Location[1]:
                if (random.random()<=organism.Mating):
                    Organisms.append(OrganismClass.Organism(False,organism.Location[0],organism.Location[1],organism,organism.Type))

    




        
        
        if organism.Fitness<=0:
            Organisms.remove(organism)
            del(organism)

    

            
        

    for pellet in Foods:
        pellet.Update()
        pygame.draw.rect(screen, pellet.Color, pygame.Rect(pellet.Location[0], pellet.Location[1], 2, 2))
        if pellet.Fitness<=0:
            Foods.remove(pellet)
            del(pellet)


    for organismk in Organisms:
        for organisml in Organisms:
            if organismk.Location[0]==organisml.Location[0]:
                if organismk.Location[1]==organisml.Location[1]:
                    if organismk.Type!=organisml.Type:
                        if organismk.Size>organisml.Size and organismk.Fitness>organisml.Fitness:
                            organismk.Fitness=organisml.Fitness+(organisml.Fitness/20)
                            Organisms.remove(organisml)
                            del(organisml)
                            print "Headshot"
                        else:
                            organisml.Fitness=organisml.Fitness-(organismk.Fitness/20)
                            organismk.Fitness=organismk.Fitness-(organisml.Fitness/20)
                            
                        

    for organism in Organisms:
        for pellet in Foods:
            if pellet.Location[0]==organism.Location[0]:
                if pellet.Location[1]==organism.Location[1]:
                    organism.Fitness=organism.Fitness+pellet.Energy
                    if organism.Fitness>organism.Max:
                        organism.Fitness=organism.Max
                    Foods.remove(pellet)
                    del(pellet)
                    
      
    
    
    pygame.display.flip()
    end = time.time()
    TIME[ONumber]=end
    return [Organisms,Foods,Step+1,end]
L=[]
FInt=[]
FVision=[]
FMax=[]
FAge=[]
FMating=[]
for j in range(20):
    print j
    Organisms=[]

    Foods=[]
    TempS=[]
    Temp1S=[]
    Temp2S=[]
    Temp3S=[]
    Temp4S=[]


    for i in range(50):
        Organisms.append(OrganismClass.Organism(True,random.randint(10,590),random.randint(10,590),0,"Samiran"))


    for i in range(20):
         Foods.append(food.Food(random.randint(10,590),random.randint(10,590)))

         
    for i in range(400):
        Iteration(Organisms,Foods,i)

    try:
        
        FInt.append(TempS)
        FVision.append(Temp1S)
        FMax.append(Temp2S)
        FAge.append(Temp3S)
        FMating.append(Temp4S)
        
    except NameError:
        FInt=TempS
        FVision=Temp1S
        FMax=Temp2S
        FAge=Temp3S
        FMating=Temp4S
        
FInt=np.sum(FInt,axis=0)
FVision=np.sum(FVision,axis=0)
FMax=np.sum(FMax,axis=0)
FAge=np.sum(FAge,axis=0)
FMating=np.sum(FMating,axis=0)

FInt=FInt/20.0
FVision=FVision/20.0
FMax=FMax/20.0
FAge=FAge/20.0
FMating=FMating/20.0

L=[FInt,FVision,FMax,FAge,FMating]
pickle.dump( L, open( "save.txt", "wb" ) )

pygame.quit()
