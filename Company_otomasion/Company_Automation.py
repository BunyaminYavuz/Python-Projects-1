class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calısma = True

    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calısanEkle()
        if secim == 2:
            self.calısanCıkar()
        if secim == 3:
            self.verilecekMaasGoster()
        if secim == 4:
            self.maaslarıVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        secim = int(input("***** {} Otomasyonuna Hos Geldiniz! *****\n\n1-Calısan Ekle\n2-Calısan Cıkar\n3-Verilecek Maas Goster\n4-Maasları Ver\n5-Masraf Gir\n6-Gelir Gir\n\nSeciminizi Gırınız: ".format(self.ad)))
        while secim < 1 or secim > 6:
            secim = int(input("Lutfen 1-6 arasında belirtilen seceneklerden birini giriniz: "))
        return secim

    def calısanEkle(self):
        id = 1
        ad = input("Calısanın adını giriniz: ")
        soyad = input("Calısanın soyadını giriniz: ")
        yas = input("Calısanın yasını giriniz: ")
        cinsiyet = input("Calısanın cinsiyetini giriniz: ")
        maas = input("Calısanın maasını giriniz: ")

        with open("calısanlar.txt", "r") as dosya:
            calısanListesi = dosya.readlines()

        if len(calısanListesi) == 0:
            id = 1
        else:
            with open("calısanlar.txt", "r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1


        with open("calısanlar.txt", "a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))

    def calısanCıkar(self):
        with open("calısanlar.txt", "r") as dosya:
            calısanlar = dosya.readlines()

        gCalısanlar = []

        for calısan in calısanlar:
            gCalısanlar.append(" ".join(calısan[:-1].split("-")))

        for calısan in gCalısanlar:
            print(calısan)

        secim = int(input("Lutfen cıkarmak istediginiz calısanın numarasını(id) giriniz(1-{}): ".format(len(gCalısanlar))))
        while secim < 1 or secim > len(gCalısanlar):
            secim = int(input("Lutfen cıkarmak istediginiz calısanın numarasını(id) giriniz(1-{}): ".format(len(gCalısanlar))))

        calısanlar.pop(secim - 1)

        sayac = 1

        dCalısanlar = []

        for calısan in calısanlar:
            dCalısanlar.append(str(sayac) + calısan.split(")")[1])
            sayac += 1

        with open("calısanlar.txt", "w") as dosya:
            dosya.writelines(dCalısanlar)


    def verilecekMaasGoster(self,hesap = "a"):
        '''hesap: a ise aylık, y ise yıllık hesap'''
        with open("calısanlar.txt","r") as dosya:
            calısanlar = dosya.readlines()

        maaslar = []

        for calısan in calısanlar:
            maaslar.append(int(calısan.split("-")[-1]))

        print("Bu ay toplam verilecek maas: {}".format(sum(maaslar)))


    def maaslarıVer(self):
        pass

    def masrafGir(self):
        pass

    def gelirGir(self):
        pass


sirket = Sirket("Bunyamin Yavuz")

while sirket.calısma:
    sirket.program()

