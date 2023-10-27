# YOLOv8 Veri Artırma Kılavuzu

Bu kılavuz, YOLOv8 nesne algılama modeli için mevcut verinizi artırmak ve veri artırma işlemiyle ilgili adımları
anlatır. Veri artırma, modelinizin daha iyi öğrenmesine ve daha yüksek doğruluk elde etmesine yardımcı olabilir.

## Gereksinimler

Bu veri artırma kılavuzunu kullanabilmek için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3.x
- YOLOv8 kurulu ve çalışır durumda
- İlgili veri seti: Bu kılavuz, "base_path" ve "destination_path" olarak adlandırılan iki ana klasörle çalışır. "
  base_path", orijinal veri setinizi içerirken "destination_path", artırılmış veri setini içerecektir. Ayrıca, "
  base_path" içinde "images" ve "labels" adlı iki alt klasörün bulunması gerekmektedir.

## Dosya Düzeni

Proje, aşağıdaki dosya düzenini bekler:

```
base_path/
|-- images/
|   |-- image1.jpg
|   |-- image2.jpg
|   |-- ...
|-- labels/
|   |-- image1.txt
|   |-- image2.txt
|   |-- ...
```

## Kullanım

1. Bu repo'yu klonlayın veya gerektiğinde indirin.

2. "base_path" klasörüne orijinal görüntüleri ve etiket dosyalarını yerleştirin.

3. Ana dizinde bu komut dosyasını çalıştırın:

```
python augmentation.py
```

5. İşlem tamamlandığında, "destination_path" klasöründe artırılmış veri setini ve etiketlerini bulabilirsiniz.

## Örnek Kullanım
Aşağıda, veri artırma işleminin nasıl kullanılacağına dair örnek bir komut bulunmaktadır:

```
python augmentation.py
```
Bu komut, "base_path" klasöründeki orijinal veri setini kullanarak "destination_path" klasöründe artırılmış veri setini
oluşturur.

## Mix Örnek Kullanımı
Birden fazla yöntemi bir arada kullanmak istiyorsanız, kodunuzu şu şekilde yazabilirsiniz:

```
brightness.mix(saturation.mix(hue.mix(exposure.mix(count=1), count=1), True)
```
Oluşacak görselin örnek ismi şu şekilde olacaktır:

```
image1-exposure-0.9358-hue-0.915-saturation-1.0685-brightness-0.9676.jpg
```
Mix fonksiyonunun 3 parametresi mevcuttur:

1. classes: Eğer burada istenilen işlemden önce başka bir yöntem kullanılmak isteniyorsa, istenilen methodun sınıfı
oluşturulup bu kısma yazılmalıdır.

2. is_last: Bu parametre sadece en dıştaki alanda kullanılmalıdır ve işlemin sona yaklaştığını anlaması için eklenmiştir.

3. count: Veri miktarı eğer güncellenmek istenirse diye eklenmiş bir alandır.

## Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LİSANS](LICENSE.txt) dosyasını inceleyin.

## Katkıda Bulunma
Katkıda bulunmak için [contributions-tr.md](contributions-tr.md) dosyasını inceleyin. Katkıda bulunmaktan çekinmeyin!

## İletişim
Soru veya önerileriniz için lütfen iletişime geçin:

Muhammet Mustafa KOÇ <br>
E-posta: mmstfkc23.61@gmail.com

Bu README dosyası, YOLOv8 ile veri artırma işlemi hakkında detaylı bilgi sağlar ve kullanıcılara adımları açıklar.
Lütfen gereksinimleri, kullanım talimatlarını, lisans bilgilerini ve iletişim bilgilerini projenize göre düzenleyin.