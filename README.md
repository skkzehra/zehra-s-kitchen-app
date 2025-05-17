# 👩‍🍳 Zehra'nın Mutfağı - Python Tabanlı Yemek Tarifi Uygulaması

Zehra'nın Mutfağı, Python programlama dili ve Tkinter/CustomTkinter kütüphaneleri kullanılarak geliştirilmiş, kullanıcı dostu bir yemek tarifi yönetim uygulamasıdır. Bu uygulama, kullanıcıların tarif eklemesine, aramasına, değerlendirmesine ve malzeme listelerini görüntülemesine olanak tanır. Veriler, MySQL veritabanında saklanır, böylece güvenli ve kalıcı bir çözüm sunulur.

## 🌟 Öne Çıkanlar

* **Modern ve Kullanıcı Dostu Arayüz:** CustomTkinter ile tasarlanmış şık ve sezgisel bir kullanıcı arayüzü.
* **Kapsamlı Tarif Yönetimi:** Tarif ekleme, arama, değerlendirme ve malzeme listesi görüntüleme gibi temel işlevler.
* **Veritabanı Entegrasyonu:** MySQL ile güvenli ve verimli veri saklama.
* **Kullanıcı Hesapları:** Kayıt ve giriş sistemi ile kişiselleştirilmiş deneyim.
* **Karanlık Mod Desteği:** Göz yorgunluğunu azaltan modern tasarım.

## 🧱 Kullanılan Teknolojiler

* **Python 3.x:** Uygulamanın temelini oluşturan, okunabilir ve güçlü bir programlama dili.
* **Tkinter & CustomTkinter:** Modern ve özelleştirilebilir kullanıcı arayüzleri oluşturmak için kullanılan GUI kütüphaneleri. CustomTkinter, Tkinter'in görünümünü iyileştirerek daha çekici bir deneyim sunar.
* **MySQL:** Güvenilir ve yaygın olarak kullanılan açık kaynaklı veritabanı yönetim sistemi.
* **Pillow (PIL):** Görüntü işleme yetenekleri sağlayan, ikonlar ve arka plan görselleri gibi görsel öğelerin yönetimi için kullanılır.

## ⚙️ Özellikler

* **👤 Kullanıcı Girişi & Kayıt Olma:**
    * Güvenli kullanıcı yönetimi ile sisteme erişimi kontrol altına alır.
    * Kullanıcılar, kendi hesaplarını oluşturabilir ve geçerli kimlik bilgileriyle sisteme giriş yapabilir.

    <img src="https://github.com/skkzehra/zehra-s-kitchen-app/blob/main/yemek_tarifi/ss/Ekran%20Resmi%202025-05-17%2013.19.53.png" alt="Giriş Ekranı" width="400">

* **📄 Tarif Ekleme:**
    * Kullanıcılar, yeni yemek tarifleri ekleyebilirler.
    * Tarif adı, malzemeler ve tarif içeriği gibi bilgiler kaydedilir.

* **🔍 Tarif Arama:**
    * Kullanıcılar, tarif adına göre arama yaparak istedikleri tariflere kolayca ulaşabilirler.

    <img src="https://github.com/skkzehra/zehra-s-kitchen-app/blob/main/yemek_tarifi/ss/Ekran%20Resmi%202025-05-17%2013.37.15.png" alt="Tarif Arama Ekranı" width="400">

* **⭐ Tarif Değerlendirme:**
    * Kullanıcılar, tarifleri 1-5 arasında puanlayabilirler.

    <img src="https://github.com/skkzehra/zehra-s-kitchen-app/blob/main/yemek_tarifi/ss/Ekran%20Resmi%202025-05-17%2013.24.20.png" alt="Tarif Değerlendirme Ekranı" width="400">

* **📝 Malzeme Listesi Görüntüleme:**
    * Kullanıcılar, bir tarifin malzeme listesini görüntüleyebilirler.

    <img src="https://github.com/skkzehra/zehra-s-kitchen-app/blob/main/yemek_tarifi/ss/Ekran%20Resmi%202025-05-17%2013.25.07.png" alt="Malzeme Listesi Ekranı" width="400">

* **🧑‍🍳 Kullanıcı Profili:**
    * Kullanıcılar, kendi profillerini görüntüleyebilir ve kaydettikleri tarifleri listeleyebilirler.

    <img src="https://github.com/skkzehra/zehra-s-kitchen-app/blob/main/yemek_tarifi/ss/Ekran%20Resmi%202025-05-17%2013.25.43.png" alt="Kullanıcı Profili Ekranı" width="400">

* **❓ Yardım ve Hakkında:**
    * Uygulama kullanımı hakkında bilgiler ve uygulama hakkında detaylar sunulur.

* **🌙 Dark Mode Desteği:**
    * Kullanıcı tercihine göre ayarlanabilen, göz yorgunluğunu azaltan modern karanlık tema desteği.

* **🏠 Ana Ekran:**
    * Uygulamanın temel işlevlerine kolay erişim sağlayan merkezi bir ekran.

    <img src="https://github.com/skkzehra/zehra-s-kitchen-app/blob/main/yemek_tarifi/ss/Ekran%20Resmi%202025-05-17%2013.21.48.png" alt="Ana Ekran" width="400">

## 🗄️ Veritabanı Yapısı

Uygulama, verileri düzenli ve verimli bir şekilde saklamak için aşağıdaki tabloları kullanır:

* **`users`:** Kullanıcı bilgilerini (kullanıcı adı, şifre) saklar.
* **`recipes`:** Yemek tarifi bilgilerini (tarif adı, malzemeler, içerik) saklar ve tarifin hangi kullanıcı tarafından eklendiğini kaydeder.
* **`ratings`:** Tariflere verilen puanları saklar.

## 🚀 Kurulum ve Çalıştırma

1.  Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install customtkinter pillow mysql-connector-python
    ```

2.  Veritabanı bağlantı ayarlarını (host, user, password, database) `connect_db()` fonksiyonunda güncelleyin.
3.  Uygulamayı çalıştırın:

    ```bash
    python zehranin_mutfagi.py # veya uygulamanızın adı
    ```

## 🧑‍💻 Geliştirici

\[Zehra Işık]

\[isikkzehraa@gmail.com]
