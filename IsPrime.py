x = int(input("Number"))

i=1
NumberOfDev=0
while i <= x/2:
    if (x % i) == 0:
        NumberOfDev=NumberOfDev+1
    i=i+1
if NumberOfDev>2:
    print("Is not prime")
else:
    print("Is prime")
    
