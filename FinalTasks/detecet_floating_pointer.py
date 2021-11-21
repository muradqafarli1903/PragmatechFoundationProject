def truefunc():
    return True
def falsefunc():
    return False





n=int(input('nece eded daxil etdiyinizi yazin: '))
arr=[]
for i in range(n):
    float_number=input('ededleri daxil edin: ')
    arr.append(float_number)
for eded in arr:
    try: 
        eded=float(eded)
        a=truefunc()
        print(a)
        
    except:
        a=falsefunc()
        print(a)



