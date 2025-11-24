#Search
import re
txt="The rain in Sapin"
x=re.search("The Sapin $",txt)
if x:
    print("Ok")
else:
    print("Not Ok")