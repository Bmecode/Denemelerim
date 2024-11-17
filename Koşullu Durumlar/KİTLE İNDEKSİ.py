print("""
*************************
Beden Kitle İndeksi Hesaplama
*************************
""")

boy=float(input("Boyunuz:"))
kilo=float(input("Kilonuz:"))
kitle_indeksi =float(kilo / boy**2)
print(kitle_indeksi)
if(kitle_indeksi <18.5):
    print("Zayıf")
elif(kitle_indeksi <25):
    print("Normal")
elif(kitle_indeksi <30):
    print("Fazla Kilolu")
elif(kitle_indeksi>=30):
    print("Obez")
else:
    print("Hatalı Giriş Yaptınız.")
