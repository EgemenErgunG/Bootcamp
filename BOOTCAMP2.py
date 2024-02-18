# -*- coding: utf-8 -*-

class Kütüphane:
    def __init__(self):
        self.dosya_adi = "Kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitap_listele(self):
        self.dosya.seek(0)
        Kitaplar = self.dosya.readlines()
        if not Kitaplar:
            print("Kayıtlı kitap yok")
            return
        print("Kitap Listesi:")
        for kitap in Kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            print(f"Başlık: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}")                  

    def kitap_ekle(self):
        kitap_adı = input("Kitabın adını giriniz: ")
        yazar = input("Kitabın yazarını giriniz: ")
        yayin_yili = input("Kitabın yayınlandığı yılı giriniz: ")
        sayfa_sayisi = input("Kitabın sayfa sayısını giriniz: ")
        kitap_bilgisi = f"{kitap_adı},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitap eklendi.")
        
    def kitap_sil(self):
        kitap_adı = input("Silmek istediğiniz kitabın adını giriniz: ")
        self.dosya.seek(0)
        Kitaplar = self.dosya.readlines()
        guncellenmis_Kitaplar = []
        silindi = False
        for kitap in Kitaplar:
            if kitap_adı in kitap:
                silindi = True
                continue
            guncellenmis_Kitaplar.append(kitap)
        if silindi:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(guncellenmis_Kitaplar)
            print(f"'{kitap_adı}' adlı kitap başarıyla silindi.")
        else:
            print(f"'{kitap_adı}' adlı kitap bulunamadı.")

        
lib = Kütüphane()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil")
    print("4) Çıkış")
    secim = input("Seçiminizi girin: ")

    if secim == "1":
        lib.kitap_listele()
    elif secim == "2":
        lib.kitap_ekle()
    elif secim == "3":
        lib.kitap_sil()
    elif secim == "4":
        del lib  
        print("Çıkış yapılıyor")
        break
    else:
        print("Geçersiz seçim. Tekrar deneyiniz.")                             #Python diline yeni başladığımdan dolayı class kısımlarını çoğunlukla chatgbt gibi yerlerden ve internetten yardım alarak tamamlayabildim.
                                                                               