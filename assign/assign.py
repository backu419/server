words=open('file.txt','r')
lines=words.readlines()
dictionary = {}
for line in lines:
    li=line.split()
    p=li[0]
    q=li[1]
    dictionary[p]= q
print(dictionary)
s1="up"
s2="down"
print(s1 +" "+s2)
for line in lines:
    if s1 and s2 in line:
        li=line.split()
        print(li[0],end=" ")
        print(li[1])
print(s1)
for line in lines:
    if s1 in line:
        li=line.split()
        print(li[0])
print(s2)
for line in lines:
    if s2 in line:
        li=line.split()
        print(li[1])
