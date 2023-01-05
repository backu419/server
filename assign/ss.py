import re
words=""""SW Forwarding: 100/0/0/0, Other: 0/0/0
 HW Forwarding:   0/1000/0/0, Other: 0/0/0"""
pattern='....'
li=words.split()
l=[]
num=[]
for line in li:
    if re.search(pattern, line):
        print()
        l.append(line)
for i in l:
    n=re.search(r'\d+',i)
    num.append(n.group(0))
print('Sucess rates in the context were: ')
print(num)
