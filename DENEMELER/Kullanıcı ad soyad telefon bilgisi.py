def kullanicibilgi():
    while True:
        ad=input("Adınız:")
        soyad=input("Soyadınız:")
        numara=int(input("Numaranız:"))

        print("Bilgileriniz")
        print("Adınız:{}\nSoyadınız:{}\nNumaranız:{}".format(ad,soyad,numara))
kullanicibilgi()