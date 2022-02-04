ax=input('enter a number:')
try:
    ival = int(ax)
except:
    ival = -1
    
if ival>0:
    print('yes')
else:
    print('no')
