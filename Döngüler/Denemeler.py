print("""
Mükemmel sayı bulma

""")
sayi=int(input("Sayı:"))
toplam=0
a=1
while sayi > a:
    if sayi % a==0 :
        toplam+=a
    a+=1
if toplam==sayi:
    print("Mükemmeldir.")
else:
    print("Mükemmel değil.")
