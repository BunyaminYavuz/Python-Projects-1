# MP3 Calar

# Kullanılan hazır fonksiyon
from random import choice

# Class yapısı
class MP3_Calar():
    def __init__(self,sarkıListesi = []):
        self.suanCalanSarkı = ""
        self.ses = 100
        self.sarkıListesi = sarkıListesi
        self.durum = True


    # Sarkı secimi
    def sarkıSec(self):
        sayac = 1
        for sarkı in self.sarkıListesi:
            print("{}{}".format(sayac, sarkı))
            sayac += 1

        secilenSarkı = int(input("Silmek istediginiz sarkının numarasını giriniz: "))

        while secilenSarkı < 1 or secilenSarkı > len(self.sarkıListesi):
            secilenSarkı = int(input("Secmek istediginiz sarkının dogru numarasını giriniz: "))

        self.suanCalanSarkı = self.sarkıListesi[secilenSarkı - 1]


    # Ses duzeyi artırma
    def sesArtır(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10

    # Ses duzeyi azaltma
    def sesAzalt(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10

    # Random sarkı secimi
    def rastgeleSarkıSec(self):
        rastgeleSarkıSecimi = choice(self.sarkıListesi)
        self.suanCalanSarkı = rastgeleSarkıSecimi


    # Sarkı ekleme
    def sarkıEkle(self):
        sanatcı = input("Sanatcıyı/Grubu giriniz: ")
        sarkı = input("Sarkıyı giriniz:")

        self.sarkıListesi.append(sanatcı + " - " + sarkı)


    # Sarkı silme
    def sarkıSil(self):
        sayac = 1
        for sarkı in self.sarkıListesi:
            print("{}{}".format(sayac, sarkı))
            sayac += 1

        silinecekSarkı = int(input("Silmek istediginiz sarkının numarasını giriniz: "))

        while silinecekSarkı < 1 or silinecekSarkı > len(self.sarkıListesi):
            silinecekSarkı = int(input("Silmek istediginiz sarkının dogru numarasını giriniz: "))

        self.sarkıListesi.pop(silinecekSarkı - 1)

    # Sistemi sonlandırma
    def kapat(self):
        self.durum = False

    # Secenekleri menu seklinde gorme
    def menuGoster(self):
        print('''
---Bunyamin Yavuz Mp3  Hos Geldiniz ---
Sarkı Listesi : {}
Suan Calan Sarkı : {}
Ses Duzeyi : {}

1-Sarkı sec
2-Sesi artır
3-Sesi azalt
4-Rastgele sarkı sec
5-Sarkı ekle
6-Sarkı sil
7-Kapat
'''.format(self.sarkıListesi,self.suanCalanSarkı,self.ses))

    # Menude secimi kullanıcıdan alma islem numarası kullanılarak
    def secim(self):
        sec = int(input("Seciminizi giriniz: "))

        while secim < 1 or secim > 6:
            sec = int(input("Seciminizi giriniz(1-7): "))

        return sec


    # Sistemi olusturan fonksiyonları cagırma merkezi
    def calıstır(self):
        self.menuGoster()
        secim = self.secim()

        if  secim  == 1:
            self.sarkıSec()

        if  secim  == 2:
            self.sesArtır()

        if  secim  == 3:
            self.sesAzalt()

        if  secim  == 4:
            self.rastgeleSarkıSec()

        if  secim  == 5:
            self.sarkıEkle()

        if  secim  == 6:
            self.sarkıSil()

        if  secim  == 7:
            self.kapat()


# Class'a obje atama
mp3calar = MP3_Calar()

# Sistemi calısır halde tutan dongu
while mp3calar.durum :
    mp3calar.calıstır()

# Sistemin sonlanmasının bildirisi
print("Mp3 kapandı")






