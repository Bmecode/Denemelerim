toplam=0
while True:
    sayı =input("Sayı Giriniz:")
    if sayı== "q" :
        break
    sayı=int(sayı)
    toplam+=sayı

    print("Sayıların Toplamı:",toplam)
