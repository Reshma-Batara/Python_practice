l=[]#creates empty list
print(l)

l=list(range(0,10))#range(start,end+1,step)
print(l)

l1=list(range(0,11,2))#gives list of elements from 0 to 10 in step of 2
print(l1)
l=[2,4,6,8,10]
l.clear()#clears list
print(l)

del l#deletes l

l=[2,4,1,"Apple","Banana",10,"Tiger"]
print(l[3])
print(len(l))
for i in l:
    print(i)
l=list("Bengaluru")
print(l)
l=["apple","orange","grapes","kiwi","papaya"]
print(l[:4])#prints the list from apple to kiwi
if "orange" in l:
    print("Yes, orange is in l")
if "mango" in l:
    print("Yes,mango is in l")
else:
    print("No,mango is not in l")
l1=[1,3,5,7,9]
l1.append(11)#adds an element 11 at the end
print(l1)
l1.insert(1,0)#inserts an element 0 at the index 1
print(l1)
l1.remove(9)#removes 9
print(l1)
l1.pop()#removes element at the end
print(l1)
l2=[2,4,6,8]
l1.extend(l2)
print(l1)
list=[10,20,30,40,50]
list.reverse()#reverses the list
print("Reverse list :",list)

l=[10,50,100,75,89,46,72,24,13,9]
l.sort()#sorts elements in ascending order
print(l)
l1=["a","B","k","L","r"]
l1.sort()
print(l1)

list=["Ant","ox","Owl","dog","CAT"]
list.sort()
print(list)
