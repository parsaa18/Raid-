# Raid 0

inp=input('enter the thing you want to save:')

s1=''
s2=''
for i in range(len(inp)):
    if i%2==0:
        s1+=inp[i]
    if i%2==1:
        s2+=inp[i]
with open('Disk1.txt','w') as dsk1:
    dsk1.write(s1)

with open('Disk2.txt','w') as dsk2:
    dsk2.write(s2)
