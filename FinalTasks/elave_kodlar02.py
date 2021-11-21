#bu proqramda ise sistem terefinden her hansi random bir eded verilir ve istifadeci hemin ededi tapmaga calisir. 7 texmin haqqi verilir. texmin haqqi biterse oyun qutarir


import random
import time
print("""**********************

say texmin oyunu
1 ile 40 arasinda ededi texmin edin



***********************""")
rand_eded=random.randint(1,40)
texmin_haqqi=7
while True:
    texmin=int(input("texmininiz: "))
    if (texmin<rand_eded):
        print("melumat arastirilir")
        time.sleep(1)
        print("daha boyuk eded deyin")
        texmin_haqqi-=1
    elif(texmin>rand_eded):
        print("melumat arasdirilir ")
        time.sleep(1)
        print("daha kicik eded deyin ")
        texmin_haqqi-=1
    else:
        print("melumat arasdirilir ")
        time.sleep(1)
        print("tebrikler",rand_eded)
        break
    if texmin_haqqi==0:
        print("texmin haqqiniz bitdi ")
        print("Eded: ",rand_eded)
        break
