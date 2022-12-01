#while loop
a=1
while a<10:
   print(a)  #use ctrl+c to break infinite loop
a+=1
print("")
#for loop
#print(iter(1)) int object is not iterable
name="harshita"
name.__iter__()
for c in name:
    print(c)
for i in range(5):
    print(i)

print("")
for i in range(5):
    print(i)
    if i==3:
        break
print("****")
for i in range(5):
    print(i)
    del i
print("")
for i in range(5):
    print(i)
    i=100
    print(i)
print("")
if True:
    pass
print('rest of the code')
print("")
for i in range(5):
    if i==3:
        break
else:                #for loop can also have break statement
    print("something")    

