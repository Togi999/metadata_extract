📌 2025 ve Sonrası İçin Dijital Adli Bilişimde Metadata Analizi ve Medya Delil Değerlendirme Trendleri

Bu çalışma, dijital adli bilişim alanında görsel/işitsel dosyaların metadata'larının analizi ve bu dosyaların delil olarak değerlendirilmesi sürecinde ortaya çıkan en güncel teknikleri incelemektedir. Bu teknikler, proje kapsamında geliştirilecek araca doğrudan entegre edilebilir niteliktedir.

🔟 2025’e Yönelik En Güncel 10 Teknik / Trend
1. Otomatik Metadata Normalizasyonu
Açıklama: Farklı cihazlardan gelen EXIF, XMP ve MediaInfo metadata'larının standart biçime çevrilmesi.

Önemi: Heterojen kaynaklardan gelen veriler tutarlı hale getirilerek analiz kolaylaşır.

Uygulama: JSON tabanlı normalize yapılar, adli raporlamada tek formatta çıktı sağlar.

Kaynak: [NIST Digital Evidence Standards Initiative, 2024]

2. EXIF ve MediaInfo Tabanlı AI Sınıflandırması
Açıklama: Yapay zekâ algoritmalarıyla metadata’ya bakarak dosyanın içerik türü (belge, tatil fotoğrafı, gözetim videosu vb.) sınıflandırılır.

Önemi: Yüz binlerce dosya arasında öncelikli olanları bulmayı kolaylaştırır.

Uygulama: Projede makine öğrenmesi modeline EXIF/MediaInfo parametreleri verilir.

Kaynak: [IEEE ICDF2C 2024]

3. GPS Verisinin Dinamik Haritalandırılması
Açıklama: GPS içeren görsellerin otomatik olarak harita üzerinde işaretlenmesi.

Önemi: Olay yeri analizi, zaman/mekân eşleşmesi kolaylaşır.

Uygulama: Google Maps API entegrasyonu ile EXIF konum verileri eşlenir.

Kaynak: [SANS DFIR GPS Geolocation Whitepaper, 2024]

4. Metadata Değişiklik Tespiti (Metadata Tamper Detection)
Açıklama: Dosya metadata'sında oynama yapılıp yapılmadığını tespit eden kontrol sistemleri.

Önemi: Delil olarak kullanılacak dosyaların sahteciliğe karşı güvenliğini artırır.

Uygulama: Hash değerleri ve zaman damgalarıyla kıyaslama yapılır.

Kaynak: [NIST SP 800-101 Rev.2]

5. JSON Tabanlı Forensik Metadata Raporlama
Açıklama: Klasik TXT/CSV raporlamaya ek olarak, yapılandırılmış JSON çıktılar ile veri aktarımı kolaylaştırılır.

Önemi: API tabanlı sistemlerle daha kolay entegre olur.

Uygulama: Otomatik rapor modülü JSON ve CSV birlikte üretir.

Kaynak: [Autopsy JSON Plugin Docs]

6. HEIC ve Yeni Medya Formatlarına Uyumluluk
Açıklama: HEIC, WebP, AVIF gibi yeni medya formatlarındaki metadata'ların da çıkarılabilmesi.

Önemi: Modern cihazlarla çekilen medya dosyaları sıkça bu formatlarda oluyor.

Uygulama: libheif, exiftool ve mediainfo güncel sürümleri entegre edilir.

Kaynak: [ExifTool v12.80 Changelog, 2025]

7. WBF (Write Blocked Forensics) Uyumlu Metadata Çıkarımı
Açıklama: Sadece okunabilir (write-blocked) ortamlardan metadata çıkarımı yapabilme.

Önemi: Adli süreçte dosyanın orijinalliğini korur.

Uygulama: Disk imajı üzerinde çalışan pytsk3 veya afflib destekli okuma yapılır.

Kaynak: [Digital Forensics with Open Source Tools, 3rd Edition]

8. Zamana Dayalı Olay Eşleme (Timeline Correlation)
Açıklama: Metadata içindeki zaman bilgilerine göre olay akışı oluşturma.

Önemi: Soruşturma sürecinde zaman çizelgesi oluşturulmasını kolaylaştırır.

Uygulama: Çekim tarihleri, oluşturulma zamanı, değiştirilme zamanı otomatik sıralanır.

Kaynak: [Plaso (log2timeline) Docs]

9. Medya Dosyalarında Ses ve Görüntü Hashing
Açıklama: Görsel/sesli dosyaların içerik hash’leri ile orijinallik doğrulaması yapılır.

Önemi: Dosyanın değiştirilip değiştirilmediğini kanıtlar.

Uygulama: aHash, pHash, SHA256 gibi görsel/ses hash algoritmaları kullanılır.

Kaynak: [ACM Digital Evidence Techniques, 2024]

10. GUI Destekli Metadata Gözlem Paneli
Açıklama: Kullanıcının klasördeki tüm medya dosyalarının metadata’larını görsel arayüzle inceleyebilmesi.

Önemi: Teknik olmayan adli personel için kullanım kolaylığı sağlar.

Uygulama: Tkinter, PyQt veya Electron ile metadata paneli tasarımı.

Kaynak: [DFRWS 2024 Demo Sessions]

