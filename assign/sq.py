# import re
# words="""SW Forwarding: 100/0/0/0, Other: 0/0/0
#  HW Forwarding:   0/1000/0/0, Other: 0/0/0"""
# pattern='....'
# li=words.splitlines()
# l=[]
# num=[]
# for line in li:
#     if re.search(pattern, line):
#         print(line)
# for i in li:
#     n=re.search(r'\d+',i)
#     num.append(n.group(0))
# print('Sucess rates in the context were: ')
# print(num)
import re
words="""SW Forwarding: 100/0/0/0, Other: 0/0/0
 HW Forwarding:   0/1000/0/0, Other: 0/0/0"""
pattern='....'
li=words.splitlines()
l=[]
for line in li:
    if re.search(pattern, line):
        l.append(line)
for i in l:
    if re.search(pattern,i):
        print(l[i])
print(li[1])
print(l)