from abc import abstractmethod
import math 

class vehicle : 
    def __init__(self, brand, model ) :
        self.brand = brand
        self.model = model


    def display_info(self):
        return f"vehicle : {self.brand} and {self.model}"
    

    def start_engine(self):
        return "Engine Started. "


class Car(vehicle):

    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def display_info(self):
        basic_info = super().display_info()  
        return f"{basic_info} and A max Speed: {self.max_speed} km/h"
    
    def __repr__(self):
        basic_info = super().display_info()  
        return f"{basic_info} and A max Speed: {self.max_speed} km/h"   


    def start_engine(self):
        return "Car Engine has Started vroom vroom"
    @abstractmethod
    def refill (self) :
        pass



Car1 = Car ("Mercedes", "X3", 300)
print(Car1.display_info())
print(Car1)

class Electric_Car(Car) :
    def __init__(self, brand, model, max_speed, range, recharge_rate):
        super().__init__(brand, model, max_speed)
        self.range = range
        self.recharge_rate = recharge_rate
    def __repr__(self):
        basic_info = super().__repr__()
        return f"{basic_info} and range : {self.range} with the respective recharge_rate : {self.recharge_rate}"
    def refill (self) :
        max_recharge = self.range - (self.range * 0.1)
        time = (max_recharge / self.recharge_rate ) * 60
        return time
    
Electric_Car1= Electric_Car("Mercedes" ,"EQS", 100, 550,100)
print ("AICI", Electric_Car1)
print (Electric_Car1.refill())      

def time_estimator(Car, distance):
    if type(Car).__name__==Electric_Car.__name__ : 
        max_recharge = Car.range - (Car.range * 0.1)
        #rechargeOneTime =  Car.refill() / max_recharge 
        #rechargeOneTime = math.ceil( rechargeOneTime)
        rechargeTotalTime= math.ceil(Car.range  / (max_recharge)* (Car.refill()))
        travel_time =(distance / math.ceil (Car.max_speed )) * 60
        time_final = (rechargeTotalTime + travel_time )
        return f"Total time in minutes is: {time_final}, and the travel time is : {travel_time} with the recharge time is : {rechargeTotalTime} "
    else :
        raise TypeError(f"You use the wrong instance of for the{type(Car).__name__} you should have used{Electric_Car.__name__}")
v=vehicle("ADSDs","Dsad")
print(time_estimator(v, 200))






    

