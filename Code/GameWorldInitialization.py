import OrganismClass
import random
import food
import json,httplib
import pickle


Gameworlds=[]
Organisms=[]

Foods=[]

for i in range(50):
    Organisms.append(OrganismClass.Organism(True,random.randint(10,590),random.randint(10,590),0,"Samiran"))
for i in range(50):
    Organisms.append(OrganismClass.Organism(True,random.randint(10,590),random.randint(10,590),0,"Gagan"))

for i in range(20):
     Foods.append(food.Food(random.randint(10,590),random.randint(10,590)))

Gameworlds.append([Organisms,Foods,[]])




connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/GameWorld', json.dumps({
 "Organisms": len(Organisms), "ID":1, "Step":0,"Data":pickle.dumps(Gameworlds[0])
     
     }), {
       "X-Parse-Application-Id": "uPZr2Zy35i3oJ7epJVQEQ3nG2MQBx1cH0QWCEHJx",
       "X-Parse-REST-API-Key": "uO6pBk2Ho9h712qgoqaxKOVu1jRNkROyu9asNF44",
       "Content-Type": "application/json"
     })




Organisms=[]

Foods=[]

for i in range(100):
    Organisms.append(OrganismClass.Organism(True,random.randint(10,590),random.randint(10,590),0,"Anudeep"))


for i in range(30):
     Foods.append(food.Food(random.randint(10,590),random.randint(10,590)))
Gameworlds.append([Organisms,Foods,[]])

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/classes/GameWorld', json.dumps({
 "Organisms": len(Organisms), "ID":2, "Step":0,"Data":pickle.dumps(Gameworlds[1])
     
     }), {
       "X-Parse-Application-Id": "uPZr2Zy35i3oJ7epJVQEQ3nG2MQBx1cH0QWCEHJx",
       "X-Parse-REST-API-Key": "uO6pBk2Ho9h712qgoqaxKOVu1jRNkROyu9asNF44",
       "Content-Type": "application/json"
     })
