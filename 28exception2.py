#Program with exception handling using try---except
a=100;b=0
try:
    print("Begin")
    print("Ready to do Division")
    c=a/b 
    print("Result=",c)
    print("Division Completed")
    print("End")
except:
    print("You cannot divide a number with zero")