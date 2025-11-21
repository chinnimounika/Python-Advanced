#Bird
class Bird:
    def fly(self):
        print("They fly to fulfill natural activities")
parrot=Bird() 
parrot.fly() 
print("Data Type of Bird=",type(Bird)) 
print("Data Type of Parrot=",type(parrot))
print("Is instance of=",isinstance(parrot,Bird))     