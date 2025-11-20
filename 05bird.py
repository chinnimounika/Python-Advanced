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