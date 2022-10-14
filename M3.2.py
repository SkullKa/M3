
l = [1,4,1,6,"hello", "a",5, "hello"]
l_unique = []

for i in l :
    count = 0
    for x in l :
        if x == i :
            count += 1
    l_unique.append(count)

l_nonunique = set()
j = 0
while j < len(l) :
    if l_unique[j] != 1 :
        l_nonunique.add(l[j])
    j += 1

print(l_nonunique)

from random import *
n = 5
 
M = [] 
 
for i in range(1, n + 1):
    line = []
    for j in range(1, n + 1):
        line = line + [randint(1, 100)]
    M = M + [line]
 
for i in range(0, n):
    for j in range(0, n):
        print(f" {M[i][j]:4d}", end="")
    print()
 
 
max_number = M[0][0]
 
for i in range(0,n):
    for j in range(0,n):

        if M[i][j] > max_number:
                max_number = M[i][j]
 
print("максимальное число = ", max_number)


l = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
j = {}
for k, v in l.items():
    j[v] = k
print(j)