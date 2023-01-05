words=open('file.txt','r')
lines=words.readlines()
s1="up"
s2="down"
c=0
for line in lines:
    if s1 and s2 in line:
        li=line.split()
        print(li[0],end=" ")
        print(li[1])
    elif s1 in line:
        li=line.split()
        print(li[0])
    elif s2 in line:
        li=line.split()
        print(li[1])