# Sistem tarihinden güncel yılı almak için date sınıfını içe aktar.
from datetime import date

# Adı metin olarak al ve baştaki/sondaki boşlukları temizle.
ad = input("Adınız: ").strip()

# Boş ad girildiğinde program açıklayıcı bir mesaj verir.
if not ad:
    print("Lütfen adınızı boş bırakmayın.")
else:
    # Sistem tarihinin yalnızca yıl bilgisini al.
    bu_yil = date.today().year
    try:
        # input() metin verir; int() metni tam sayıya dönüştürür.
        dogum_yili = int(input("Doğum yılınız: "))
    except ValueError:
        # Harf veya ondalıklı sayı girildiğinde kullanıcıyı uyar.
        print("Doğum yılını tam sayı olarak girin.")
    else:
        # Doğum yılı pozitif olmalı ve güncel yılı geçmemeli.
        if not 1 <= dogum_yili <= bu_yil:
            print(f"Doğum yılı 1 ile {bu_yil} arasında olmalı.")
        else:
            # Yıl farkı, kişinin bu takvim yılında dolduracağı yaştır.
            yas = bu_yil - dogum_yili
            # f-string, adı ve hesaplanan yaşı mesaja yerleştirir.
            print(f"Merhaba {ad}! Bu yıl {yas} yaşını dolduruyorsun.")
