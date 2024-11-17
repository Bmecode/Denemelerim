def armstrong():
    print("""
    **********************************
    ARMSTRONG SAYILARI BULMA PROGRAMI
    **********************************
    
    Programı sonlandırmak için 'q' tuşuna basınız.
    """)

    while True:
        sayi=input("Bir Sayı Giriniz:")
        if sayi == "q":
            print("Program Sonlandırılıyor...")
            break
        toplam=0
        basamak_sayisi=len(sayi)
        for i in sayi:
            c=int(i)
            toplam+= c**basamak_sayisi
        if (toplam==int(sayi)):
            print("ARMSTRONG Sayısıdır.")
        else:
            print("ARMSTRONG Sayısı Değildir.")
print(armstrong())