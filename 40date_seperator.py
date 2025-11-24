#Program to print current date with seperator as/
from datetime import date
d=date.today()
print("Year=",d.year)
print("Month=",d.month)
print("Day=",d.day)
print(d.year,"/",d.month,"/",d.day)