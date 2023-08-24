
# Cloudflare Check
Bu proje, verilen web sitelerinin Cloudflare kullanıp kullanmadığını tespit eden bir Python aracını içermektedir. Cloudflare, birçok web sitesinin güvenliğini ve performansını artırmak amacıyla kullandığı bir içerik dağıtım ağı ve güvenlik hizmetidir. Bu araç, belirli URL'leri kontrol ederek, sunucu başlıkları üzerinden Cloudflare hizmetinin kullanılıp kullanılmadığını belirler.

## Proje Özellikleri
Tekil URL Kontrolü: Projeyi kullanarak belirli bir URL'nin Cloudflare hizmeti kullanıp kullanmadığını kontrol edebilirsiniz. Eğer URL geçerli bir formatta değilse veya bağlantı sırasında zaman aşımına uğrarsa, durumu hakkında bilgi verilir.

Dosya Tabanlı Kontrol: Proje, bir dosyada bulunan URL listesini okuyarak bu URL'lerin Cloudflare kullanıp kullanmadığını denetler. Bu özellik sayesinde büyük URL listelerini otomatik olarak analiz edebilirsiniz.

### Gereksinimler
Bu projenin çalışması için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

argparse: Komut satırı argümanlarını işlemek için kullanılır.

requests: HTTP istekleri göndermek ve almak için kullanılır.

### Komut Satırı Argümanları
```
-d, --domain: Tek bir URL'nin Cloudflare durumunu kontrol etmek için kullanılır.

-i, --input: Bir dosyadan URL listesi alarak Cloudflare durumunu kontrol etmek için kullanılır.

-h, --help: Yardım mesajlarını görmek için kullanılır. 
```

### Örnek Kullanım
> #### Tekil URL Kontrolü:

```python cloudflare_check.pt --domain https://example.com```

![]()

> #### Dosya Tabanlı Kontrol:

```python cloudflare_check.pt --input https://example.com```

![]()

