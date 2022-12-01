n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
print("")


for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,j-1),end=" ")
    print()

for i in range(n):
    for j in range(n):
        print(max(i,j),end=" ")
    print()
    for i in range(n):
    for j in range(n):
        print(j,end = " ")
    print()