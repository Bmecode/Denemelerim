def geometriksekil ():
    while True:
        print("Geometrik Şekil Hesaplama")
        şekil=input("Üçgen mi Dörtgen mi:")
        if şekil=="Dörtgen":
            a=int(input("1. Kenarı giriniz:"))
            b=int(input("2.kenarı giriniz:"))
            c=int(input("3.kenarı giriniz:"))
            d=int(input("4.kenarı giriniz:"))
            if (a==b and a==c and a==d):
                print("Kare")
            elif (a==c and b==d):
                print("Dikdörtgen")
            else:
                print("Dörtgen")
        elif şekil=="Üçgen":
            a=int(input("1.Kenarı Giriniz:"))
            b=int(input("2.Kenarı Giriniz:"))
            c=int(input("3.Kenarı Giriniz:"))
            if abs(a+b)>c and abs(a+c)>b and abs(b+c)>a:
                if(a==b and a==c):
                    print("Eşkenar Üçgen")
                elif(a==b and a!=c)or(a==c and a!=b)or(b==c and b!=a):
                    print("İkizkenar Üçgen")
                else:
                    print("Çeşitkenar Üçgen")
            else:
                print("Üçgen Belirtmiyor")

        else:
            print("Hatalı Giriş Yaptınız...")
geometriksekil()