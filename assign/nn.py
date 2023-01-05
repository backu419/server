import re
my_str = """SW Forwarding: 100/0/0/0, Other: 0/0/0 
HW Forwarding:   0/1000/0/0, Other: 0/0/0"""
text="the Hcl is in chennai in "
x=re.findall("^T.*e$",text)
print(x)


lines=my_str.split()
pattern='....'
a=[]
c=0
for line in lines:
    c+=1
    if (re.search(pattern, line)):
        if (c==3 or c==8):
            a.append(line)
print(a)
# # one
# # two
# # three
# for line in lines:
#     print(line)
# d=list(filter())