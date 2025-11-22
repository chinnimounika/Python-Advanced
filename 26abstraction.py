class Bank:
    def irate(self):
        pass
class HDFC(Bank):
    def irate(self) :
      print("Interest Rate of HDFC is 8%")
class ICICI(Bank):
    def irate(self):
        print("Interest Rate of ICICI is 10.2%")
H=HDFC() 
I=ICICI()
H.irate()
I.irate()               