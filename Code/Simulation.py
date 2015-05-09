import pickle
from pylab import *
TIME = pickle.load( open( "time.p", "rb" ) )
import random

#Heuristics Leader Election:2s Mapping: 2s Iteration=MAX(TIME)=3s
'''
MULTIPLES=[]
for i in range(1000):
    MULTIPLES.append((i+1)*7)

plot(MULTIPLES)
xlabel('Steps')
ylabel('Time')

grid(True)

show()
'''

for i in range(len(TIME)):
    TIME[i]=float(TIME[i])

'''
ML=[]
for i in range(500):
    ML.append(0)
for i in range(1):
    if i%100==0:
        for j in range(500):
            ML[j]=ML[j]-(2.0/TIME[j])
    for j in range(500):
        ML[j]=ML[j]+(1.0/TIME[j])
        for k in range(int (1.0/TIME[j])):
            for l in range (j):
                if random.random<0.0067:
                    try:
                        ML[j+1]=ML[j]
                        ML[j-1]=ML[j]
                        ML[j]=ML[j]-(2.0/TIME[j])
                        ML[j+1]=ML[j+1]-(2.0/TIME[j+1])
                        ML[j-1]=ML[j-1]-(2.0/TIME[j-1])
                    except IndexError:
                        pass
plot(ML)
xlabel('Time')
ylabel('Steps')

grid(True)

show()
           


'''

#fig = plt.figure(figsize=(7, 7))


#plt.ion()



ML=[]

for i in range(500):
    ML.append(0)



plt.plot(ML)
plt.show(block=False)
Actual=[]

Waiting=[]
Frozen=[]
for i in range(500):
    Actual.append(random.randint(200,400))

for i in range(7000):
    
    if i%100==0 and i!=0:
        for j in range(500):
            ML[j]=ML[j]-(2.0/TIME[Actual[j]])
    


        
        
    for j in range(500):
        if j not in Frozen:
            ML[j]=ML[j]+(1.0/TIME[Actual[j]])
            IT=(1.0/TIME[Actual[j]])
            if IT<=1:
                if random.random()<IT:
                    IT=1
            else:
                IT=int(IT)
       
            for k in range(int(IT)):
                for l in range (Actual[j]):
                    if random.random()<0.0067:
                    
                        try:
                        
                            if ML[j+1]>=ML[j]:
                     
                                ML[j+1]=ML[j]
                           
                              
                            else:
                                if ML[j+1]<ML[j]:
                                    Frozen.append(j)
                                
                        except IndexError:
                            if ML[0]>=ML[j]:
                     
                                ML[0]=ML[j]
                           
                              
                            else:
                                if ML[0]<ML[j]:
                                    Frozen.append(j)
        Frozen=dict.fromkeys(Frozen).keys()
        for m in Frozen:
            try:
                if ML[m+1]>=ML[m]:
            
                    ML[m+1]=ML[m]
                    Frozen.remove(m)
            except IndexError:
                if ML[0]>=ML[m]:
            
                   ML[0]=ML[m]
                   Frozen.remove(m)
                            
                            
                          
          
    temp="Time: "+str(i)                       
    plt.xlabel(temp)         
    plt.plot(ML)
    plt.draw()

plot(ML)
xlabel('Time')
ylabel('Steps')

grid(True)

show()

print min(ML)         
print sum(ML)/len(ML)
print max(ML)
