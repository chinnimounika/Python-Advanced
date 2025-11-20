class Bird:
    def fly(self):
        print("They fly to fulfill natural activities")
    def buildnest(self):
        print("They build nest to live")    
parrot=Bird()
parrot.age=5
parrot.wings=2
parrot.wt=4.5
parrot.color="GREEN"
print("Age of Parrot=",parrot.age)
print("Wings of Parrot=",parrot.wings)
print("Weight of Parrot=",parrot.wt)
print("Color of Parrot=",parrot.color)
parrot.fly()  
parrot.buildnest() 
print("_________________________________________________")
pigeon=Bird()
pigeon.age=3
pigeon.wings=2
pigeon.wt=6
pigeon.color="GREY"
print("Age of Pigeon=",pigeon.age)
print("Wings of Pigeon=",pigeon.wings)
print("Weight of Pigeon=",pigeon.wt)
print("Color of Pigeon=",pigeon.color)
pigeon.fly()  
pigeon.buildnest() 
