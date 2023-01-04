#create an empty tuple:
t=()
print(t)

t=23,54,665,643,7,5
for i in t: #iterates over t
    print(i)
    
l=[1,2,3,4,5]
t=tuple(l)
print(t)
#methods on tuple:
t=(1,2,3,23,43,4,12,24,5,8,10,7,20,11)
print(len(t))
print(t.count(24))#gives the number of repitions of an element
print(t.index(43))
t1=sorted(t)
print(t1)
#tuple packing
a=10
b=15
c=20
t=(a,b,c)
print(t)
#tuple unpacking:
t=(50,60,70,80)
w,x,y,z=t
print(w)
print(x)
print(y)
print(z)
