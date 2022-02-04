from random import randint

# Oyunun aktif olup olmadıgını kontrol eder
oyunDurumu = True

while oyunDurumu :
    # Baslangıc degeri
    tahminAralıgıBas= int(input("Baslangıc degerini giriniz : "))

    # Bitis degeri
    tahminAralıgıSon = int(input("Bitis degerini giriniz : "))

    # Baslangıc ve bitis degerini aralık seklinde parametrelendirme
    rastgeleSayı = randint(tahminAralıgıBas,tahminAralıgıSon)

    # Tahmin etme hakkınızı giriniz
    tahminHak = int(input("Tahmin etme hakkınızı giriniz : "))

    while True :

        if tahminHak > 0 :

            tahmin = int(input("Sizce sayı kac ? "))


        else:

            print("Sayıyı tahmin edemediniz !:(sayı {}".format(rastgeleSayı))
            break


        if tahmin != rastgeleSayı :

            tahminHak -= 1

            if tahmin > rastgeleSayı :

                print("Sayı asagıda ! Kalan tahmin hakkınız {}".format(tahminHak))

            else:

                print("Sayı yukarıda ! Kalan tahmin hakkınız {}".format(tahminHak))


        else:

            print("Tebrikler ! Sayıyı buldunuz.")
            break

    kontrol = input("Oyunu tekrar oynamak ister misiniz ?(E/H):")

    if kontrol == "E":

        oyunDurumu = True

    else:
        oyunDurumu = False
