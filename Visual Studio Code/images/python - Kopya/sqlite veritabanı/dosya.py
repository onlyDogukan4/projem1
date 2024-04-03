import tkinter as tk

class HamMaddesi:
    def __init__(self, adi, profili, saç_levhasi):
        self.adi = adi
        self.profili = profili
        self.saç_levhasi = saç_levhasi
        self.stok_miktari = 0  # Stok miktarını başlangıçta 0 olarak ayarla

    def ham_madde_giris(self, miktar):
        if miktar < 0:
            return f"Hata: {miktar} miktarı negatif olamaz."
        else:
            self.stok_miktari += miktar  # Stok miktarını güncelle
            return f"{self.adi} hammadde {miktar} adet girdi. Stok: {self.stok_miktari} adet"

    def ham_madde_çikis(self, miktar):
        if miktar < 0:
            return f"Hata: {miktar} miktarı negatif olamaz."
        elif self.stok_miktari < miktar:
            return f"Hata: Stokta yeterli {self.adi} hammadde yok. Stok: {self.stok_miktari} adet"
        else:
            self.stok_miktari -= miktar  # Stok miktarını güncelle
            return f"{self.adi} hammadde {miktar} adet çıktı. Stok: {self.stok_miktari} adet"

# Tkinter arayüzü oluşturma
def miktar_girisi():
    miktar = miktar_entry.get()
    miktar = int(miktar) if miktar.isdigit() else 0
    secilen_hammadde = hammadde_combobox.get()
    sonuc_label.config(text=ham_maddeler[secilen_hammadde].ham_madde_giris(miktar))
    stok_label.config(text=f"Stok: {ham_maddeler[secilen_hammadde].stok_miktari} adet")

def miktar_cikisi():
    miktar = miktar_entry.get()
    miktar = int(miktar) if miktar.isdigit() else 0
    secilen_hammadde = hammadde_combobox.get()
    sonuc_label.config(text=ham_maddeler[secilen_hammadde].ham_madde_çikis(miktar))
    stok_label.config(text=f"Stok: {ham_maddeler[secilen_hammadde].stok_miktari} adet")

# Ana uygulama penceresi oluşturma
app = tk.Tk()
app.title("Hammadde İşleme Arayüzü")

# Birden fazla hammadde için örnekler oluşturup bir sözlükte saklama
ham_maddeler = {
    "1.ürün": HamMaddesi("1.ürün", "15 cm", "45 gr"),
    "2.ürün": HamMaddesi("2.ürün", "Özellik2", "Miktar2"),
    "3.ürün": HamMaddesi("3.ürün", "Özellik3", "Miktar3"),
    "4.ürün":HamMaddesi("4.ürün","özellik4","Miktar4"),
    # ---------------Diğer ürünleri buraya Ekleyeceksiniz--------------
}

# Stok miktarını göstermek için bir ComboBox (kombinasyon kutusu) ekleme
hammadde_combobox = tk.StringVar(app)
hammadde_combobox.set("1.ürün")  # Başlangıçta seçilen hammadde
hammadde_optionmenu = tk.OptionMenu(app, hammadde_combobox, *ham_maddeler.keys())
hammadde_optionmenu.pack()

# Giriş çıkış miktarı girmek için giriş alanı ve düğmeleri oluşturma
miktar_label = tk.Label(app, text="Miktar:")
miktar_label.pack()

miktar_entry = tk.Entry(app)
miktar_entry.pack()

giris_button = tk.Button(app, text="Stoğa ekleme Yap", command=miktar_girisi)
giris_button.pack()

cikis_button = tk.Button(app, text="Stoktan Düş", command=miktar_cikisi)
cikis_button.pack()

# Stok gösterme etiketi
stok_label = tk.Label(app, text=f"Stok: {ham_maddeler['1.ürün'].stok_miktari} adet")
stok_label.pack()

# Sonuç gösterme etiketi
sonuc_label = tk.Label(app, text="")
sonuc_label.pack()

app.mainloop()