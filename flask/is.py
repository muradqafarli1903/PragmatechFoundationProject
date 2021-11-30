class isci():
    def __init__(self,ad,maas,departament):
        print("isci sinifinin init funksiyasi cagirildi")
        self.ad=ad
        self.maas=maas
        self.departament=departament
    def melumatlarigonder(self):
        print("Isci sinifinin melumatlari...")
        print("Ad: {}\nMaas: {}\nDepartament:{}".format(self.ad,self.maas,self.departament))
    def departament_deyistir(self,yeni_departament):
        self.departament=yeni_departament
class yonetici(isci):
    pass
yonetici1=yonetici("Murad","1500","IT")
yonetici1.melumatlarigonder()
yonetici1.departament_deyistir("muhasibat")
yonetici1.melumatlarigonder()