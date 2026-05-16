# Vibecoding Fun

## Proje Hakkında

Bu proje Flask backend ve sade HTML/CSS/JS arayüzleriyle çalışan küçük bir LLM uygulamasıdır. Tek seferlik LLM çağrısı, history tutan asistan ve tool-calling agent sayfaları içerir.

Agent artık `analyze_text` aracını kullanabilir. Bu araç verilen metindeki kelime sayısı, cümle sayısı, karakter sayıları, ortalama kelime uzunluğu ve en uzun kelimeyi hesaplar; böylece agent metin istatistiği isteyen konuşmalarda görünür bir tool call yapar.

## Kurulum

Projeyi çalıştırmak için gereksinim dosyasındakı paketlerin kurulması gerekmektedir. Bunun için:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

komutunu çalıştırarak gerekli tüm bağımlılıkları yükleyebilirsiniz.

## Kullanım

Proje, arka planda `app.py`, `agent.py`, `asistan.py` ve `llm.py` Python dosyaları ve ön yüzde `frontend` klasöründeki HTML dosyaları ile çalışmaktadır. Her bir bileşen spesifik işlemler için tasarlanmıştır.

```
flask --app app run --debug
```

Agent arayüzü için `http://127.0.0.1:5000/agent` adresini açın. Örnek test konuşması: `Şu metni analyze_text aracıyla analiz et: Merhaba dünya! Bugün hava çok güzel.`

## Test

Otomatik testler `pytest` ile çalışır:

```
python3 -m pytest
```

## Katkıda Bulunma

Katkıda bulunmak isteyenler standart bir pull request süreci üzerinden projeye katkıda bulunabilirler.

## Lisans

Bu projeye ait lisans bilgileri burada yer alacaktır.
