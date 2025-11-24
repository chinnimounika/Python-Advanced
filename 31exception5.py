#User Defined Exception
class InvalidAgeException(Exception):
    pass
age=int(input("Enter Your Age:"))
try:
    if(age<18):
        raise InvalidAgeException
except:
    print("Not Ok")
else:
    print("ok")
finally:
    print("Ask others to Vote")            