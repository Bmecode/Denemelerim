range(0,20) # 0'dan 20' a kadar (dahil değil) sayı dizisi oluşturur.
l= list(range(0,20)) # list fonksiyonuyla listeye dönüştürebilir.
print(l)
print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.
for i in range(10):
	print(i)

for i in range(10):
    print("*" * i)
