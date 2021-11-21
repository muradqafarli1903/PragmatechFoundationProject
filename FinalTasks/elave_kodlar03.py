#bu proqramda helelik 3 emeliyyat yazmisam. birincisi balansi yoxlayir ikincisi balansi artirir, ucuncu ise balansdan pul cixir. proqram istifadeci 'q'-ye basana qeder davam edir.

print("""*********************

ATM  


*************************
1. Balansi yoxlama
2. pul kocurtme 
3. Mexaric 
  Proqramdan cixmaq ucun 'q'e basin
*******************""")
balans=1000
while True:
    emeliyyat =input("emeliyyati secin ")
    if (emeliyyat=="q"):
        print("Yene gozleyirik... ")
        break
    elif(emeliyyat== "1"):
        print(" balansiniz {} manatdir. ".format(balans))
    elif(emeliyyat=="2"):
        miqdar= int(input("miqdari daxil edin  "))
        balans+=miqdar
    elif(emeliyyat=="3"):
        miqdar=int(input(" miqdari daxil edin "))
        if (balans-miqdar<0 ):
            print("balansinizi artirin. ")
            continue
        balans-=miqdar
    else:
        print("ugursuz emeliyyat ... ")
