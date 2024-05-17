class car () : 
    def start (self) :
        print ("VROOM VROOM")
        
    def __init__(self, CP, Year ):
        self.Year = Year 
        self.CP = CP
from random import randint        
def factory() :
    ls = []
    for nr in range (100) :
        Year = randint (1990, 2024)
        CP = randint (90,200)
        
        masina = car(CP, Year)
        ls.append(masina)
    return ls
ls=factory()
for car in ls:
    (car).start()

    
