import math
j=input("Zadaj mi priemer podstavy: ")
j=int(j)
x=j/2
y=input("Zadaj mi výšku valca: ")
x=int(x)
y=int(y)
podstava=math.pi*(x**2)
plast=(2*math.pi)*x*y
povrch=(podstava+plast)*2
plechovky=povrch/7.5
print("Na natrenie fontánky treba ",plechovky," plechoviek.")
