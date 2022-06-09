#  Menu
print('Type 1 To Use Raid 0')
print('Type 2 To Use Raid 1')
print('Type 3 To Use Raid 10')
print('Type 4 To Exit')
c=int(input('Choose:'))
while True:
    if c==1:
        print('you chose Raid 0')
        break
    elif c==2:
        print('you chose Raid 1')
        break
    elif c==3:
        print('you chose Raid 10')
        break
    elif c==4:
        print('Bye then')
        exit()
        
    else:
        c=int(input('Select Between 1-4:'))
        
