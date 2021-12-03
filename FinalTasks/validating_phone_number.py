nomre_sayi=int(input('nomrenin sayini daxil edin: '))
arr=[]
for i in range(nomre_sayi):
    nomre=input('nomreni daxil edin: ')
    arr.append(nomre)
    
for nomre1 in arr:

    if nomre1[0]!='7' and nomre1[0]!='8' and nomre1[0]!='9' :
        print('nomre 7,8 ve 9la baslamalidir')
    elif len(nomre1) != 10:
        print('nomre 10 reqemden ibaret olmalidir')
    else: 
        print('nomre duzgundur')
try:
        nomre=int(nomre)
except:
    print('nomrede simvol istifade oluna bilmez ')


        