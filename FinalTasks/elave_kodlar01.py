#en boyuk ortaq bolunenin tapilmasi proqrami. Bu kodlar diger kodlarda sehv cixarsa hemin kodlarin yerine doldurulmasi ucun yazilir
def ebob_tapma(eded1,eded2):
    i=1
    ebob=1
    while(eded1>=i and eded2>=i ):
        if (eded1%i==0 and eded2%i==0):
            ebob=i
        i+=1
    return(ebob)
eded1=int(input("ededi daxil edin: "))
eded2= int(input("2.ededi daxil edin "))
print("ebob= ",ebob_tapma(eded1,eded2))
