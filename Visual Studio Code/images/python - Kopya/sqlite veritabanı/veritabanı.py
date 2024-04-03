import sqlite3
con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (Ürün_Adı TEXT,Fiyat İNT,Stok_Sayısı İNT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into Kitaplık Values('Karton Bardak',650,7)")
    con.commit()
def veri_ekle2(Ürün_Adı,Fiyat,Stok_Sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?)",(Ürün_Adı, Fiyat, Stok_Sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste=cursor.fetchall()
    print(liste)
def verileri_al2():
    cursor.execute("Select Ürün_Adı,Fiyat From kitaplık")
    liste=cursor.fetchall()
    print(liste)
def verileri_guncelle(Ürün_Adı,Yeni_Adı):
    cursor.execute("Update kitaplık set Ürün_Adı=? where Ürün_Adı=?",(Yeni_Adı,Ürün_Adı))
    con.commit()

#Ürün_Adı=input("Ürün_Adı:")
#Fiyat=int(input("Fiyat:"))
#Stok_Sayısı=int(input("Stok_Sayısı:"))

def verileri_sil(Ürün_Adı):
    cursor.execute("Delete From kitaplık where Ürün_Adı=?",(Ürün_Adı,))
    con.commit()







tablo_olustur()
#veri_ekle2(Ürün_Adı,Fiyat,Stok_Sayısı)

def verileri_al3(Fiyat):
    cursor.execute("select * from kitaplık where Fiyat=?",(Fiyat,))
    liste=cursor.fetchall()
    for i in liste:
       print(i)
#veri_ekle2(Ürün_Adı,Fiyat,Stok_Sayısı)
#verileri_al()

#verileri_guncelle("Karton_Bardak","Kapkartonnnnn bardak")
#verileri_guncelle("",)
verileri_sil("'")
verileri_al()



con.close()
