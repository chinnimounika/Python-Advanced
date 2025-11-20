class IceCream:
    def melt(self):
        print("It melts at room temperature")
    def billamt(self):
        return self.price*self.quantity  
vanilla=IceCream()
vanilla.price=20
vanilla.quantity=500
vanilla.wt=45.5
vanilla.color="Vanilla White" 
print("Price of Vanilla=",vanilla.price) 
print("Quantity of Vanilla=",vanilla.quantity)
print("Weight of Vanilla=",vanilla.wt)
print("Color of Vanilla=",vanilla.color)
print("Bill amount of Vanilla=",vanilla.billamt())
vanilla.melt()
print("_______________________________________________")
Pista=IceCream()
Pista.price=30
Pista.quantity=400
Pista.wt=40.5
Pista.color="Pista green" 
print("Price of Pista=",Pista.price) 
print("Quantity of Pista=",Pista.quantity)
print("Weight of Pista=",Pista.wt)
print("Color of Pista=",Pista.color)
print("Bill amount of Pista=",Pista.billamt())
Pista.melt()
print("_________________________________________________")