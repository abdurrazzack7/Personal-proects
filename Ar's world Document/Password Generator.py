import random
Uppercase="ABDCDEFGHIJKLMNOPQRSTUYWXYZ"
lowercase="abcdefghijklmnopqrstuywxyz"
Number="0123456789"
Symbol ="!@#$%^" 

ans=Uppercase+lowercase+Number+Symbol

length=8
password = "".join(random.sample(ans,length))
print("The Generated Password is: ",password)
