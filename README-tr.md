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

- `base_path`: Ana veri dizini.
    - `images`: Görsel dosyalarının bulunduğu alt dizin. Dosyaların .jpg veya .jpeg uzantısına sahip olması
      gerekmektedir.
    - `labels`: Etiket dosyalarının bulunduğu alt dizin. Dosyalar, ilgili görsellerle aynı isme sahip .txt uzantısına
      sahip olmalıdır.

```
base_path/
|-- images/
| |-- image1.jpg
| |-- image2.jpg
| |-- ...
|-- labels/
| |-- image1.txt
| |-- image2.txt
| |-- ...
```

## Kullanım

1. Bu repo'yu klonlayın veya gerektiğinde indirin.
2. YOLOv8 modelinizin kurulu olduğundan ve çalıştığından emin olun.
3. "base_path" klasörüne orijinal görüntüleri ve etiket dosyalarını yerleştirin.
4. Ana dizinde bu komut dosyasını çalıştırın.

    ```bash
    python augmentation.py
    ```

5. İşlem tamamlandığında, "destination_path" klasöründe artırılmış veri setini ve etiketlerini bulabilirsiniz.

## Örnek Kullanım

Aşağıda, veri artırma işleminin nasıl kullanılacağına dair örnek bir komut bulunmaktadır:

  ```bash
  python augmentation.py
  ```

Bu komut, "base_path" klasöründeki orijinal veri setini kullanarak "destination_path" klasöründe artırılmış veri setini
oluşturur.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LİSANS](LICENSE.txt) dosyasını inceleyin.

## Katkıda Bulunma

Katkıda bulunmak için [contributions-tr.md](contributions-tr.md) dosyasını inceleyin. Katkıda bulunmaktan çekinmeyin!

## İletişim

Soru veya önerileriniz için lütfen iletişime geçin.

Muhammet Mustafa KOÇ
mmstfkc23.61@gmail.com

Bu README dosyası, YOLOv8 ile veri artırma işlemi hakkında detaylı bilgi sağlar ve kullanıcılara adımları açıklar.
Lütfen gereksinimleri, kullanım talimatlarını, lisans bilgilerini ve iletişim bilgilerini projenize göre düzenleyin.
