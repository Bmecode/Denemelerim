print("""
************************************
Kullanıcı Girişi
************************************
""")

sys_kullanıcı_adı="burakm"
sys_parola= "12345"

kullanıcı_adı= input("Kullanıcı Adı:")
parola=input("Parola:")

if(kullanıcı_adı==sys_kullanıcı_adı and sys_parola != parola):
    print("Parola Hatalı...")
elif(kullanıcı_adı!=sys_kullanıcı_adı and sys_parola==parola):
    print("Kullanıcı Adı Hatalı...")
elif(kullanıcı_adı!=sys_kullanıcı_adı and sys_parola!=parola):
    print("Kullanıcı Adı ve Parola Hatalı")
else:
    print("Sisteme başarıyla giriş yapıldı...")
