import sqlite3 as sql
# bağlanacak olduğumuz veri tabanının adını yazıyoruz eğer sistemde adını yazdığımız veri tabanı yoksa yazılan adda bir veri tabanı oluşturuluyor
vt= sql.connect('kitaplik_db.sqllite')
imlec=vt.cursor()
def ekle (kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik_db(kitap_id INTEGER PRIMARY KEY AUTOINCREMENT,kitap_adi,kitap_yazari,okunma_durumu,begeni)")
    kitap_girisi = "INSERT INTO kitaplik_db (kitap_adi,kitap_yazari,okunma_durumu,begeni) VALUES('"+kitap_adi+"','"+kitap_yazari+"','"+okunma_durumu+"','"+begeni+"')"
    imlec.execute(kitap_girisi)
    vt.commit()
def güncelle (guncellenecek):
    gkitap_adi=input("güncel kitap adını giriniz:")
    gkitap_yazari=input("güncel kitap yazarının giriniz:")
    gokunma_durumu=input("güncel okunma durumunu giriniz:")
    gbegeni_durumu=input("güncel beğeni durumu giriniz:")
    guncelleme_kodu="UPDATE kitaplik_db SET kitap_adi='"+gkitap_adi+"',kitap_yazari='"+gkitap_yazari+"',okunma_durumu='"+gokunma_durumu+"',begeni='"+gbegeni_durumu+"' WHERE kitap_id='"+guncellenecek+"'"
    imlec.execute(guncelleme_kodu)
    vt.commit()
def listele():
    imlec.execute("SELECT*FROM kitaplik_db ")
    kitaplar=imlec.fetchall()
    print(kitaplar)
    vt.commit()
def sil(silinecek):
    silme_kodu="DELETE FROM kitaplik_db WHERE kitap_id='"+silinecek+"'"
    imlec.execute(silme_kodu)
    vt.commit()
def cikis():
    vt.close()
    print("Çıkış yapıldı,İYİ GÜNLER")
