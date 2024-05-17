class car () : 
    on = False
    # year 
    # CP 
    # KM
    # nr_usi 
    # Name 
    def start (self) :
        print ("VROOM VROOM")
        on = True
    def __init__(self, year, CP, KM, nr_usi=5, Name='Dacia' ):
        self.year = year 
        self.CP = CP
        self.KM = KM
        self.nr_usi = nr_usi
        self.Name = Name 
    def pret(self) :
        acp = self.CP //50
        aKm = self.KM // 10000
        varsta = 2024- self.year
        const = 10000
        pret = const + (varsta* (-0.05*const)) 
        pret += acp*10
        pret += aKm*(-150)
        return pret

    
m1 = car (year=2019,CP=250,KM=78513,nr_usi=3)
m1.start ()
m1.pret ()
print(m1.pret())

