print("""
**************************
Not Ortalaması Hesaplama
**************************
""")
vize1=float(input("Vize 1 Not:"))
vize2=float(input("Vize 2 Not:"))
final_not=float(input("Final Notu:"))

ortalama=float(vize1*3/10+vize2*3/10+final_not*4/10)

print(ortalama)
if ortalama >=90:
    print("AA")
elif ortalama >=85:
    print("BA")
elif ortalama >=80:
    print("BB")
elif ortalama >=75:
    print("CB")
elif ortalama >=70:
    print("CC")
elif ortalama >=65:
    print("DC")
elif ortalama >=60:
    print("DD")
elif ortalama >= 55:
    print("FD")
else:
    print("FF")