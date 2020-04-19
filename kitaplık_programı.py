#Yazan: Geomatik Mühendisi Tunahan Sarıgül
import sys
import kitaplik_veritabanı as baglanti
print("----"*15)
print("#"*15,"KİTAPLIĞINIZA HOŞGELDİNİZ","#"*20)
print("----"*15)
while True:
    print("#"*10,"Yapmak istediğiniz işlemi seçiniz","#"*10)
    print("#"*10,"(E)klemek","(L)istelemek","(G)üncellemek","(S)ilmek","(Ç)ıkış","#"*10)
    islem=input()
    if islem== "E" or islem=="e" :
        kitap= input("Kitap adının yazınız:")
        yazar=input("Kitabın yazarını yazınız:")
        okunma_durumu=input("okunma durumunu giriniz:")
        beğenme_durumu=input("beğeni durumunu giriniz:")
        baglanti.ekle(kitap,yazar,okunma_durumu,beğenme_durumu)
    elif islem=="L" or islem=="l":
            baglanti.listele()
    if islem=="S" or islem=="s":
            baglanti.listele()
            silinecek=input("silmek istediğiniz kitabın id numarasını giriniz")
            baglanti.sil(silinecek)
    elif islem== "G" or islem=="g" :
            baglanti.listele()
            guncellenecek=input("güncellemek istediğiniz kitabın id numarasını giriniz")
            baglanti.güncelle(guncellenecek)
    if islem== "Ç" or islem=="ç" :
        baglanti.cikis()
        sys.exit()

