print("""
Mükemmel Sayı Bulma Programı

""")
sayı=int(input("Sayıyı Giriniz:"))
i=1
toplam=0

while i<sayı:
    if sayı % i ==0:
        toplam+=i
    i+=1
if(toplam==sayı):
    print(sayı,"Mükemmel sayıdır.")
else:
    print(sayı,"Mükemmel sayı değildir.")