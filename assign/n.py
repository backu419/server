# words="224.0.1.40       GigabitEthernet1/2/2     00:50:35  00:02:31  41.41.41.1"
# for line in words:
#     li = words.split()
#     p=(li[0])
#     q=(li[1])
#     r=(li[4])
# print("Interface   :"+q)
# print("Ip addresses:"+p+" "+r)
import re
# words="Distributed Forwarding Card WS-F6K-DFC4-AXL    SAL1444YCLW  0.111  Ok"
# pattern='-'
# file=words.split()
# for line in file:
#     if re.search(pattern, line):
#         print(line)
import re
# words="Distributed Forwarding Card WS-F6K-DFC4-AXL    SAL1444YCLW  0.111  Ok"
# pattern='-'
# for line in words:
#     li=words.split()
#     if re.search(pattern, line):
#         print(line)

# import re
# words="""vss1#ping ipv6 2001:10::1
# Type escape sequence to abort.
# Sending 5, 100-byte ICMP Echos to 2001:10::1, timeout is 2 seconds:
# !!!!!
# Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms
# vss1#ping ipv6 2001:10::3
# Type escape sequence to abort.
# Sending 5, 100-byte ICMP Echos to 2001:10::3, timeout is 2 seconds:
# .....
# Success rate is 0 percent (0/5)
# vss1#"""
# lines=words.splitlines()
#
# pattern="Success rate is "
# l=[]
# num=[]
# for line in lines:
#     if re.search(pattern, line):
#         l.append(line)
# for i in l:
#     n=re.search(r'\d+',i)
#     num.append(n.group(0))
# print(l)
# print(num)
import re
words="224.0.1.40       GigabitEthernet1/2/2     00:50:35  00:02:31  41.41.41.1"
# for line in words:
#     li = words.split()
#     p=(li[0])
#     q=(li[1])
#     r=(li[4])
# print("Interface   :"+q)
# print("Ip addresses:"+p+", "+r)
# pattern='...'
# li=words.split()
# c=0
# for line in li:
#     c+=1
#     if re.search(pattern, line):
#         if c<3:
#             print(line)
import re
words="224.0.1.40       GigabitEthernet1/2/2     00:50:35  00:02:31  41.41.41.1"
pattern='...'
li=words.split()
c=0
print("IP address \tInterface")
for line in li:
    c+=1
    if re.search(pattern, line):
        if c<3:
            print(line, end='\t')