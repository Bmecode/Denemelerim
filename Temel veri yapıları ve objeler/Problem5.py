birinci= int(input("Birinci Sayı:"))
ikinci= int(input("İkinci Sayı:"))
print("Değiştirilmeden Önce Değerler:\n Birinci:{} İkinci:{}".format(birinci,ikinci))
birinci,ikinci=ikinci,birinci
print("Değiştirildikten Sonra Değerler:\n Birinci:{} İkinci:{}".format(birinci,ikinci))
