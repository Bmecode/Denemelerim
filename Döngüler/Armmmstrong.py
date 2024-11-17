print(""" 
************************************
ARMSTRONG LANET OLASI SAYILARI BULMA
************************************
Çıkmak için 'e' basınız.

""")
while True:
    sayi = input("Sayı:")
    toplam = 0
    if sayi == "e":
        print("HOŞÇAKALIN...")
        break


    for i in sayi:
        a = len(sayi)
        b = int(i)

        toplam += b**a

    if toplam == int(sayi):
        print(sayi," Sayı Armstrong sayısıdır.,,")
    else :
        print(sayi,"Sayı Armstrong sayısı değildir...")