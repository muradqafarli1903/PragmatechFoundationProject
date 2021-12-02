users=[]
simvollar=['\?','\+','\*','\!','\%']


import re
import time
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class Register:
    def __init__(self,ad='murad',soyad='qafarli',password='Besiktas1903*',mail='muradq469@gmail.com',nomre='8808699',operator='50'):
        self.ad=ad
        self.soyad=soyad
        self.password=password
        self.mail=mail
        self.nomre=nomre
        self.operator=operator
        users.append(self)
    def qeydiyyat(self):
        
        print('zehmet olmasa asagidaki xanalari doldurun...')
        self.ad=input('Adiniz:(doldurulmasi zeruridir) ')
        self.soyad=input('Soyadiniz:(doldurulmasi zeruridir) ')
        self.mail=input('mail: ')
        self.operator=input('Prefiks: Nar: 70 ve ya 77, Azercell: 50,Bakcell: 55 ve ya 99 ')
        self.nomre=input('Nomre: +994 {}'.format(self.operator))
        self.password=input("sifre: (doldurulmasi zeruridir) ")
    
    def adYoxlama(self):
        
        
        while True:
            if self.ad==" ":
                print('adinizi daxil edin')
                self.ad=input('Adiniz:(doldurulmasi zeruridir) ')
            else:
                break
    def soyadYoxlama(self):
        
        while True:
            if self.soyad==" ":
                print('soyadinizi daxil edin')
                self.soyad=input('Soyadiniz:(doldurulmasi zeruridir) ')
            else:
                break
    def nomreYoxlama(self):
        
    
        while True:
            if len(self.nomre)!=7:
                self.nomre=input('duzgun nomre daxil edin: +994 {}'.format(self.operator))
            
            
            else:
                break
            try:
                self.nomre=int(self.nomre)
            except:
                self.nomre=input('nomre simvol qebul ede bilmez, yeniden cehd edin: +994 {}'.format(self.operator))
    def mailYoxlama(self):
        
    
        while True:
            if (re.fullmatch(regex,self.mail)):
                print('mail duzgundur. ')
                break
            else:
                self.mail=input('Mail yanlisdir, yeniden cehd edin')
    def sifreYoxlama(self):
        
        if len(self.password)<8:
            raise Exception('Sifre en az 8 simvol olmalidir')
        elif not re.search('[a-z]',self.password):
            raise Exception('sifrede en az bir kicik herf olmalidir')
        elif not re.search('[A-Z]',self.password):
            raise Exception('sifrede en az 1 boyuk herf olmalidir')
        elif not re.search('[0-9]',self.password):
            raise Exception('sifrede en az reqem olmalidir')
        elif not re.search(str(simvollar),self.password):
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
answer=input('istifadeci girisi: Y/N ')
while answer=='Y':
    show=Register()
    show.qeydiyyat()
    show.adYoxlama()
    show.soyadYoxlama()
    show.mailYoxlama()
    show.nomreYoxlama()
    show.sifreYoxlama()
else:
    print('error')