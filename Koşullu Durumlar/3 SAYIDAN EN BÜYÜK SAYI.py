print("""
**********************
Belirtilen 3 Sayıdan En Büyüğünü Bulma

**********************
""")

birinci=float(input("Birinci Sayı:"))
ikinci=float(input("İkinci Sayı:"))
üçüncü=float(input("Üçüncü Sayı:"))

if (birinci>=ikinci and birinci>=üçüncü):
    print("En büyük sayı:",birinci)
elif(ikinci>=birinci and ikinci>=üçüncü):
    print("En büyük sayı:", ikinci)
elif(üçüncü>=birinci and üçüncü>=ikinci):
    print("En büyük sayı:",üçüncü)