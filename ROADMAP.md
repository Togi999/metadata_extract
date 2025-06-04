# ROADMAP.md: Python ile Dijital Adli Bilişim için Metadata Çıkarımı Geliştirme ve Test Etme

## Giriş
Bu yol haritası, Python kullanılarak dijital adli bilişim süreçlerinde medya dosyalarının metadata bilgilerini (EXIF, MediaInfo vb.) çıkarmaya yönelik özelliklerin nasıl geliştirileceği ve test edileceğine dair detaylı bir rehber sunar. **Önemli Uyarı: Bu bilgiler yalnızca eğitim ve araştırma amaçlıdır. Yetkisiz kullanımı yasa dışı ve etik dışıdır. Herhangi bir sistemde veya veri üzerinde işlem yapmadan önce açık izin almanız zorunludur.**

Bu rehber, dijital medya dosyalarının metadata analizini Python ile otomatik hale getirmeyi, etik ve yasal sınırlar içinde kalarak kontrollü bir ortamda test etmeyi amaçlar.

## Ön Koşullar
- **Python 3.x**: Geliştirme için temel dil.
- **Kütüphaneler**:
  - `Pillow`: Görsel dosyaların EXIF verilerini okumak için (`pip install Pillow`).
  - `hachoir`, `mutagen`, `mediainfo`: Farklı medya türlerinden metadata almak için.
  - `folium`: GPS konumlarını haritada göstermek için (`pip install folium`).
  - `tkinter` veya `PyQt5`: Basit bir grafik arayüz için.
- **Bilgi Gereksinimleri**:
  - Python programlama temelleri.
  - Dosya sistemleri ve dosya formatları hakkında temel bilgi.
  - JSON ve CSV gibi veri formatlarıyla çalışma deneyimi.

## Test Ortamını Kurma
Güvenli bir test ortamı oluşturmak için aşağıdaki adımları izleyin:
1. **İzolasyon**: Test amaçlı kopyalanmış medya dosyaları kullanın.
2. **Veri Klasörü**: Taranacak dosyaların bulunduğu ayrı bir dizin oluşturun.
3. **Çıktı Dizinleri**: JSON, CSV ve TXT çıktılarının yazılacağı klasörleri tanımlayın.

## Temel Bileşenlerin Geliştirilmesi

### EXIF Metadata Okuyucu
Fotoğraflardan çekim tarihi, cihaz bilgisi ve GPS koordinatlarını alır.

```python
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_exif(file_path):
    image = Image.open(file_path)
    exif_data = image._getexif()
    if not exif_data:
        return {}
    return {TAGS.get(tag): val for tag, val in exif_data.items() if tag in TAGS}
```

### MediaInfo Metadata Okuyucu
Video/ses dosyalarından süre, format, çözünürlük gibi bilgiler çıkarır.

```python
from pymediainfo import MediaInfo

def extract_media_info(file_path):
    media_info = MediaInfo.parse(file_path)
    return media_info.to_data()
```

### GPS Verisini Haritada Gösterme

```python
import folium

def map_gps(lat, lon, output_html="map.html"):
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon]).add_to(m)
    m.save(output_html)
```

### Klasör Taraması ve Otomatik Metadata Çıkarımı

```python
import os

def scan_directory(folder_path):
    metadata_results = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".jpg", ".jpeg", ".png", ".mp4", ".mp3")):
                full_path = os.path.join(root, file)
                # Burada uygun extract fonksiyonlarını çağırın
                # metadata = extract_exif(full_path) veya extract_media_info(full_path)
                metadata_results.append({"file": full_path, "metadata": {}})
    return metadata_results
```

## Gelişmiş Geliştirmeler

### JSON, CSV, TXT Formatında Raporlama
Kullanıcının çıktıları tercih ettiği formata göre dışa aktarım yapılmasını sağlar.

```python
import json, csv

def export_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Dosya", "Metadata"])
        for entry in data:
            writer.writerow([entry['file'], str(entry['metadata'])])
```

### Basit GUI
Dosya seçimi, tarama ve sonuç görüntüleme için arayüz (örneğin Tkinter).

```python
import tkinter as tk
from tkinter import filedialog

# GUI örneği: kullanıcıdan klasör seçmesini isteyin
```

## Geliştirmelerin Test Edilmesi
1. **EXIF Okuyucu**:
   - EXIF içeren görsellerle test edin (ör. telefonla çekilmiş fotoğraflar).
2. **MediaInfo**:
   - MP4/MP3 dosyalarıyla süre, format gibi bilgilerin doğru alındığını doğrulayın.
3. **GPS Görselleştirme**:
   - GPS içeren dosyalarla harita çıktısını kontrol edin.
4. **Raporlama**:
   - JSON, CSV çıktılarının eksiksiz ve doğru biçimde üretildiğinden emin olun.
5. **GUI**:
   - Temel işlevlerin arayüz üzerinden erişilebilir olması test edilir.

## Karşı Önlemler ve En İyi Uygulamalar
- **Veri Gizliliği**: Kişisel verilerin korunmasına dikkat edin.
- **Yedekleme**: Orijinal dosyaları işlem öncesi yedekleyin.
- **Yasal İzin**: İncelenen her medya dosyası için kullanım izni alın.
- **Kapsamlı Test**: Her dosya türü için geniş çaplı test yapılmalı.

## Sonuç
Bu yol haritası, Python ile medya dosyalarından dijital adli bilişim amaçlı metadata çıkarımı yapmayı ve bunları anlamlı raporlar haline getirmeyi adım adım açıklamaktadır. Bilgiler etik, güvenli ve profesyonel amaçlarla kullanılmalı, geliştirmeler açık kaynak topluluklarıyla paylaşılmalıdır.
