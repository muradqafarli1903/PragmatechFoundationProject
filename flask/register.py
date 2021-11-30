users=[]
simvollar=['\?','\+','\*','\!','\%']

import re
import time
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class register:
    def __init__(self,_ad,_soyad,_password,_mail,_nomre):
        self.ad=_ad
        self.soyad=_soyad
        self.password=_password
        self.mail=_mail
        self.nomre=_nomre
        users.append(self)
    def qeydiyyat():
        global ad,soyad,mail,password,nomre,operator
        print('zehmet olmasa asagidaki xanalari doldurun...')
        ad=input('Adiniz:(doldurulmasi zeruridir) ')
        soyad=input('Soyadiniz:(doldurulmasi zeruridir) ')
        mail=input('mail: ')
        operator=input('Prefiks: Nar: 70 ve ya 77, Azercell: 50,Bakcell: 55 ve ya 99 ')
        nomre=input('Nomre: +994 {}'.format(operator))
        password=input("sifre: (doldurulmasi zeruridir) ")
    
    def adYoxlama():
        
        while True:
            if ad==" ":
                print('adinizi daxil edin')
                ad=input('Adiniz:(doldurulmasi zeruridir) ')
            else:
                break
    def soyadYoxlama():
        
        while True:
            if soyad==" ":
                print('soyadinizi daxil edin')
                soyad=input('Soyadiniz:(doldurulmasi zeruridir) ')
            else:
                break
    def nomreYoxlama():
        
    
        while True:
            if len(nomre)!=7:
                nomre=input('duzgun nomre daxil edin: +994 {}'.format(operator))
            
            
            else:
                break
            try:
                nomre=int(nomre)
            except:
                nomre=input('nomre simvol qebul ede bilmez, yeniden cehd edin: +994 {}'.format(operator))
    def mailYoxlama():
        
    
        while True:
            if (re.fullmatch(regex,mail)):
                print('mail duzgundur. ')
                break
            else:
                mail=input('Mail yanlisdir, yeniden cehd edin')
    def sifreYoxlama():
        
        if len(password)<8:
            raise Exception('Sifre en az 8 simvol olmalidir')
        elif not re.search('[a-z]',password):
            raise Exception('sifrede en az bir kicik herf olmalidir')
        elif not re.search('[A-Z]',password):
            raise Exception('sifrede en az 1 boyuk herf olmalidir')
        elif not re.search('[0-9]',password):
            raise Exception('sifrede en az reqem olmalidir')
        elif not re.search(str(simvollar),password):
            raise Exception('Sifrede en az bir simvol olmalidir: * % + ? !')
        else:
            print('Sifre yoxlanilir...')
            time.sleep(1)
            print('Sifre duzgundur')
        while True:
            try:
                pass
            except Exception as xeta:
                print(xeta)
while True:
    answer=input('qeydiyyat: Y/N')
    if answer== 'Y':

        register.qeydiyyat()
        register.adYoxlama()
        register.soyadYoxlama()
        register.mailYoxlama()
        register.nomreYoxlama()

        register.sifreYoxlama()
        print(users)
    else:
        break