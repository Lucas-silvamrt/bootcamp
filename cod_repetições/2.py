p=int(input('digite o valor inicial:'))
b=int(input('digite o valor final:'))
if p<b:
    for f in range (p,b+1):
        formula=(5*(f-32))/9
        print('\n',f,'|', formula)
else:
    for f in range (p,b-1,-1):
        formula=(5*(f-32))/9
        print('\n',f,'|', formula)
