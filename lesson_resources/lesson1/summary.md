# DERS 1 · DEĞİŞİM — Ders Özeti

> **Kurs:** AI ile Yazılım Geliştirme | **Hafta:** 1 | **Süre:** ~2 saat

---

## Slayt 1 — Başlık: "AI Yazılım Geliştirmeyi Nasıl Dönüştürdü?"

- Bu kurs, AI'nin yazılım geliştirme pratiğini nasıl dönüştürdüğünü ele alıyor — araç tanıtımı değil, paradigma değişimi odaklı.
- Kurs içeriği otomatik tamamlamadan (autocomplete) ajansal CLI'ye uzanan üç dalgayı ve beş yıllık dönüşümü kapsıyor.
- Eğitimci bu hafta Deep Learning AI konferansından (San Francisco) dönmüş; herkesin aynı soruyu konuştuğunu ama çok az çözüm önerisi olduğunu gözlemlemiş.

---

## Slayt 2 — Hakkımda

- Oğuzhan Çetinkaya: ~25 yıllık yazılım/teknoloji geliştirme deneyimi, son 10 yılda Amerika'da.
- Şu anda Automation Anywhere şirketinde **Machine Learning Architect** olarak çalışıyor.
- Bu, aynı eğitimcinin düzenlediği ikinci kurs; birincisi "AI nasıl kullanılır" üzerineydi, bu kurs "AI ile yazılım geliştirme nasıl dönüşüyor" konusunu işliyor.

---

## Slayt 3 — Bugün / Yolculuk (7 Bölüm)

- Bugünkü ders kod yazmayı değil **perspektifi** ele alıyor: ne değişiyor, neden değişiyor, biz neredeyiz?
- Gündem: paradigma kayması, tarihsel öngörüler, tarih kendini tekrar eder, fırsatlar ve sorunlar, 3 yıl önceki iş akışı, üç dalga/üç kavram, gelecek hafta ve ödev.
- Kayıtlar paylaşılmayacak; notlar ve sunumlar paylaşılacak. Ödevler Discord üzerinden takip edilecek.

---

## Slayt 4 — Manifesto: "Bu bir araç güncellemesi değil"

- Yaşanan şey yeni bir IDE ya da framework değil; **yazılım üretme şeklinin kendisi** tamamen değişiyor.
- Kim yazıyor, hangi rollerle, hangi yeteneklerle, hangi süreçle — bunların hepsi sıfırdan yeniden tanımlanıyor.
- Eğitimcinin mesajı: "Bu bir araç güncellemesi değil; bizim tam olarak yazılım geliştirme şeklimizin kendisi baştan aşağı değişiyor."

---

## Slayt 5 — Kırılım: PC → İnternet → Smartphone → AI (2022→)

- Önceki devrimler (PC, İnternet, Akıllı Telefon) bize yeni araçlar verdi; biz o araçlarla daha fazla iş yaptık.
- **AI'nin farkı:** Önceki devrimler bize araç verdi, AI ise **insanın yaptığı işin yerine geçecek şekilde** tasarlanıyor.
- Bu yüzden diğer teknoloji kırılımlarından daha tehditkâr ve daha köklü bir dönüşüm söz konusu.

---

## Slayt 6 — Öngörü 01/03: Dario Amodei (Anthropic)

- Amodei: "AI önümüzdeki 1-5 yıl içinde teknoloji, hukuk, danışmanlık ve finanstaki giriş seviyesi rollerin yarısını yok edebilir."
- Önemli nokta: kaybolan **junior level** pozisyonlar — "çırak" basamağı ortadan kalkıyor.
- Peki yarının seniorları nasıl yetişecek? Junior'dan Senior'a geçiş basamağı kayboluyor. Bu ciddi bir skill geçiş sorunu.
- Not: Bu tür keskin söylemler sahiplerinin iş çıkarları (GPU satışı, AI yatırımı) ile örtüşüyor; eleştirel bakmak gerekiyor.

---

## Slayt 7 — Öngörü 02/03: Karpathy, Altman, Huang, Microsoft %30

- **Andrej Karpathy:** Software 1.0 (kod), 2.0 (model ağırlıkları), 3.0 (Prompt) — yeni bir programlama paradigması.
- **Jensen Huang:** "Çocuklarınıza kod yazmayı öğretmeyin" — eğitimci bu söyleme katılmıyor; yazılımcıların kodu bilmesi hâlâ şart.
- **Sam Altman:** Küçük takımlar AI agent'larla milyar dolarlık şirketlerin işini yapabilir; single founder sayısı artıyor.
- **Microsoft (2025):** Kodun %30'u AI tarafından yazılıyor.

---

## Slayt 8 — Öngörü 03/03: Cursor %60, Google %75, Karpathy "İngilizce"

- **Google (2025):** Geliştirilen kodun %75'i agent'lar tarafından yazılıyor.
- **Cursor:** Aralık 2025 itibarıyla "Agent Request" oranı "Tab Accept" oranını geçti — komutla yaptırma, kabul ederek tamamlamayı solladı.
- **Karpathy:** "En popüler programlama dili artık İngilizce" — herhangi bir insan diliyle bu iş yapılabiliyor.
- Aralık 2025 bir kırılım noktası: Claude Opus ile agent'lar gerçekten bir özelliği veya bug'ı baştan sona çözebilir hale geldi.

---

## Slayt 9 — Bölüm İki Ara Slayt: "Tarih kendini tekrar eder"

- Paradigma değişikliklerini anlamak için tarihten örüntüler çıkarmak gerekiyor.
- Amaç: tarihin bize ne öğrettiğinden yola çıkarak önümüzü görebilmek.

---

## Slayt 10 — Tarih 01/03 (1450): El yazması → Matbaa

- 15. yüzyılda bir katibin tek bir İncil'i yazması **bir yıl** alıyordu; matbaayla bu süre günlere indi.
- Katiplik mesleği yok olmadı, **dönüştü**: matbaacılar, dizgiciler, yayıncılar, editörler, gazeteciler ortaya çıktı.
- Ders: beceri kayboluyor, meslek dönüşüyor — yazımın sentaksı değil, **ne yazılacağı** önem kazanıyor. Bugün yazılımda da benzer: sentaks bilgisi değil, ne üretileceği önemli.

---

## Slayt 11 — Tarih 02/03 (1900): At arabası → Otomobil

- San Francisco Polis Departmanı eskiden atlar için buğday satın alıyordu — otomobil gelince nalbantlar, ahırlar ortadan kalktı.
- Onların yerine otomobil fabrikaları, benzin istasyonları, sigortacılar, lojistik sektörü doğdu.
- Bugün de benzer: sadece kod değil, **takım yapısı, kariyer yolu, alınan eğitim** değişiyor.

---

## Slayt 12 — Tarih 03/03 (1900-1960): İnsan+hayvan → Traktör

- Tarlaları ekip biçmek için yüzlerce-binlerce insan gerekirken traktörle onlarca kişi yeterli oldu.
- Geri dönüş yok — verimlilik artışı o kadar büyük ki eski yönteme dönmek imkânsız.
- Daha az insanla daha fazla üretim: yazılım geliştirme maliyeti düşüyor ama yazılıma duyulan ihtiyaç **artıyor** (ekilmesi gereken tarla sayısı artıyor).

---

## Slayt 13 — Sentez Desen: "Hepsinde aynı geçiş"

- Tüm paradigma değişimlerinde ortak desen: el emeği → makine, mekanik → dijital, fiziksel ürün → dijital servis, yerel pazar → küresel platform.
- **Her seferinde:** eski beceri tam değersizleşmiyor ama yeni beceri çok daha değerli hale geliyor.
- Yazılım dünyasında geçiş: bireysel kod yazımından **agentic development**'a doğru gidiyoruz.

---

## Slayt 14 — Sentez Fırsat: "Krizi fırsata çevirme zamanı"

- İki seçenek var: ya bu dalganın altında kalacaksınız ya da üstüne çıkacaksınız.
- Skill setini güncelleyenler, yeni düzenin rollerine girenler çok avantajlı konuma geçebilir.
- Bir adım öte: yeni düzenin ihtiyaç duyduğu araçları, şirketleri, hizmetleri **siz üretebilirsiniz** — single founder sayısı her zamankinden fazla.
- Tsunami metaforu: yerli halk tehlikeyi görüp yükseğe çıkar; turistler video çekerken dalga hepsini alır.

---

## Slayt 15 — Fırsat Verisi: LinkedIn 2025

- LinkedIn 2025 raporuna göre **"AI Engineer"** dünyanın en hızlı büyüyen iş tanımı.
- AI Engineer tanımı: AI'ye iş yaptırabilen, çıktısını denetleyen, sistem kuran mühendis.
- Birkaç yıl önce bu unvan yoktu; şimdi tüm ünvan listelerinin tepesinde.
- Küçük takımlar (hatta tek kişi) AI agent takımıyla büyük projeler üretebiliyor — communication overhead'i sıfıra iniyor.

---

## Slayt 16 — Dürüstlük / Sorunlar: "Hızın faturası"

- En iyi AI, en iyi yazılımcıdan daha iyi kod yazmıyor — hız var ama kalite her zaman üst seviyede değil.
- **AI Slop:** Spek net değilse veya yazılımcı deneyimsizse üretilen kod çok kötü kalitede olabiliyor; güvenlik açıkları, kötü tasarım, birbiriyle aynı arayüzler ortaya çıkıyor.
- **Veri güvenliği:** Open source projeler bile AI-yazılmış pull request'leri kabul etmeyi durdurdu; Meta kendi Llama dışında araç kullandırmıyor.
- **Yönetim baskısı:** Şirketler "kodun yüzde kaçını AI yazıyor?" diye soruyor; token sayımı yapılıyor. Yönetimden AI kullanımını artırma baskısı giderek yoğunlaşıyor.
- **Teknik borç:** Çok hızlı üretim technical debt'i artırıyor; bazı projelerde ne ekip ne AI sorunları çözemiyor hale geldi.

---

## Slayt 17 — Neden Mühendislik: Grady Booch

- Grady Booch: Yazılımcıların yaşadığı "varoluşsal kriz" yeni değil — Assembly'den C'ye, compiler'lara, OOP'ye, Cloud'a kadar her geçişte aynı korku yaşandı; meslek bitmedi, dönüştü.
- **Mühendislere her zamankinden daha fazla ihtiyaç var** — AI kod yazsa da mühendislik yargısı daha değerli hale geliyor.
- Eğitimcinin notu: Grady Booch'un Pragmatic Engineer kanalındaki konuşmasını izlemenizi öneriyor.

---

## Slayt 18 — Booch'un 3 Fikri

1. **Araçlar değişiyor, problemler değişmiyor:** Sistem tasarımı, güvenlik, kalite, ölçeklenebilirlik, etik, maliyet, insan faktörünü dengelemek hâlâ mühendisliğin işi. AI bu dengeyi kuramaz.
2. **Bir soyutlama seviyesi yukarı çıkıyoruz:** Assembly → C → Python → Framework → Doğal dil. Bu yok oluş değil, yükseliş. Temellere (system design, algoritmik düşünme, veri yapıları, debugging, security) odaklanın — bunlar hiç kaybolmayacak.
3. **Kod yazmak sadece bir parça:** Yazılım mühendisliği; ne inşa etmeli, neden, nasıl güvenli/sürdürülebilir, ekonomik mi, etik mi sorularıyla ilgilenir. Kod üretimi otomasyonlaşabilir ama mühendislik yargısı daha da değerleniyor. Geleceğin mühendisi: kodlayan değil, sistemi tasarlayan, kararları veren mimar.

---

## Slayt 19 — Bölüm Üç Ara Slayt: "3 yıl önce. Sadece üç."

- Üç yıl gibi çok kısa bir sürede her şey köklü biçimde değişti.
- Bu değişim Waterfall → Agile gibi bir süreç iyileştirmesi değil; kod geliştirmenin **özü** değişti.

---

## Slayt 20 — 2022 Öncesi İş Akışı: Bir özellik 2 hafta - 2 ay

- Klasik pipeline 7 adım: PM (spec/ticket) → Tasarımcı (wireframe) → Mimar (teknik tasarım) → Developer (kod yaz, debug et, Stack Overflow) → Code Review (PR) → QA (test, "bende çalışmıyor") → DevOps/CI-CD (deploy) → Acceptance Test.
- Bir fikirden production'a: **2 hafta ile 2 ay** arası.
- Bu sistem 30 yıldır temelde aynı; Waterfall → Agile/Scrum/Kanban döngüleri küçülttü ama temeli değiştirmedi.

---

## Slayt 21 — Bölüm Dört Ara Slayt: "Üç dalga. Üç yıl."

- 2021-2025 arasında kod yazma şeklimiz üç dalga halinde değişti.
- Bu dalgaların her biri öncekini tamamen silmedi ama ağırlık merkezi hızla kaydı.

---

## Slayt 22 — Dalga 01/03 (2021-2023): GitHub Copilot — Autocomplete

- GitHub Copilot, VS Code'da extension olarak geldi; sadece **açık dosyaları** context olarak alıyordu.
- Siz yazmaya başladığınızda sonraki satırları/metotları tahmin edip tamamlıyordu; Tab'a basıp kabul ediyordunuz.
- Özellikle unit test yazımında çok pratikti.
- Karakteristik özellik: "Akış değişmedi, sadece klavye hızlandı. Asistan değildi, tamamlayıcıydı. Komut yoktu, sohbet yoktu, tahmin vardı."

---

## Slayt 23 — Dalga 02/03 (2023-2025): Cursor/Continue/Windsurf — Sohbet edilen IDE

- Cursor, Windsurf, GitHub Copilot Chat: IDE içinden **komut vererek** kod yazdırma dönemi.
- "Şu fonksiyonu yaz", "şurada hata var, düzelt" gibi komutlar veriyordunuz; AI yazıyor, siz onaylıyor ya da elle düzeltiyordunuz.
- Pair programmer gibi: siz tarif ediyordunuz, AI yazıyordu; her adımda accept/reject kontrolü sizdeydi.
- Bir özellik çok daha hızlı geliştirilebilir oldu ama her adımda insan onayı hâlâ gerekiyordu.

---

## Slayt 24 — Dalga 03/03 (Aralık 2025→): Claude Code/Opus — Ajansal CLI

- Claude Code ile terminal üzerinden çalışan agent katmanı geldi; **her adımı onaylamanıza gerek yok**.
- Agent kodu kendi okuyor, ilgili dosyaları buluyor, hipotez kuruyor, çalıştırıyor, test ediyor, başarısız olursa tekrar deniyor.
- "Bug'ı düzelt" diyorsunuz, kahvenizi alıp geliyorsunuz — kod yazımı tamamen delege edilmiş.
- Aralık 2025 kırılımı: Opus modeliyle agent'lar bir feature'ı veya bug'ı baştan sona çözebilecek yetkinliğe ulaştı. Karpathy da bu dönemde "ben de tamamen agent'larla kod yazmaya başladım" dedi.

---

## Slayt 25 — Bölüm Beş Ara Slayt: "Üç kavram. Yeni beceriler."

- Üç dalgaya paralel olarak üç yeni mühendislik kavramı doğdu.
- Hepsinin adında "Engineering" geçiyor çünkü hepsi ayrı mühendislik yetkinliği gerektiriyor.

---

## Slayt 26 — Kavram 01/03: Prompt Engineering

- ChatGPT ile hayatımıza girdi; komutu doğru kurmak bir sanattır.
- Temel unsurlar: net olmak, örnek vermek, persona/rol tanımlamak, çıktı formatını belirlemek.
- Hâlâ çok önemli ama **tek başına yetmiyor** — agent'lara prompt vermek de değişti.
- Andrew Ng bu dönemde yeni bir "AI Prompting" kursu yayınladı; prompting de modelden agent'lara geçişle birlikte evrildi.

---

## Slayt 27 — Kavram 02/03: Context Engineering

- "Sır komutta değil, agent'a verdiğin bağlamda."
- Agent'a tool'lar, MCP server'lar, skill'ler, data source'lar, conversation history veriliyor — bunların hepsi context'e giriyor.
- Context Size büyüse de (1M+ token) fazla doldurulunca model performansı düşüyor; eğitimci 200-300K'yı geçince yeniden başlıyor.
- **Context'i iyi yönetmek** kritik bir yetenek haline geldi: neyi içeri alacaksın, neyi dışarıda tutacaksın?

---

## Slayt 28 — Kavram 03/03: Harness Engineering (Agentic Engineering)

- Bu kursun **ana konusu** ve konferanslarda en çok konuşulan kavram.
- Soru artık "agent'a nasıl iş veririm?" değil, **"agent'ları çalıştıracağım sistemi nasıl kurarım?"**
- Kapsamı: hook'lar, pipeline'lar, skill'ler, agent'lar, agent team'ler — CICD ne ise bu da agent pipeline'ı.
- "Vibe Coding" kavramı geride kaldı; kimse kullanmıyor artık.
- Spec review, kod review'ın yerini alıyor: yüz binlerce satır kod üretilirken artık spec'ler review ediliyor.

---

## Slayt 29 — Sıradaki W_02: Claude Code Derinlemesine

- Gelecek hafta: Claude Code kurulumu, çalıştırma, plan'lar, skill'ler, hook'lar, prompt mühendisliği detayları.
- Spec'ten çalışan kod nasıl üretilir — uygulamalı olarak ele alınacak.
- Codex kullanımı önerisi: Claude Code 100$/ay planı yoksa Codex'in 20$/ay planı güçlü bir alternatif.

---

## Slayt 30 — İlk Ödev: Bir sayfalık spec yaz

- **Görev:** Gerçek bir problem seçin, o problem için bir sayfalık spec yazın.
- Spec içeriği: hangi problemi çözüyor, nasıl çözüyor, nasıl ekranları olacak, hangi teknoloji kullanılacak.
- Bir GitHub reposu oluşturun ve spec'i oraya koyun (Git/GitHub bilmiyorsanız hemen öğrenin — temel bir yetenek).
- Formu Discord'daki linkten doldurun ve gönderin.
- Kursun sonunda tüm derslere katılıp ödevlerini tamamlayanlar sertifika alacak.

---

## Genel Notlar / Sınıf Tartışmasından Öne Çıkanlar

- **Layoff'ların asıl nedeni AI değil:** Yüksek faiz, savaşlar, IPO yokluğu, ekonomik daralma şirketleri efficient olmaya zorluyor. Konferanstaki büyük firmaların ekiplerinde AI yüzünden iş azaldığını söyleyen kimse yoktu.
- **Junior pozisyon paradoksu:** Junior iş azalıyor ama yeni başlayanlar hızlı adapte olabildiğinden eğitimci "yeni başlayan birini alır, hemen öğretirim" diyor.
- **Temel bilginin önemi:** AI iyi kullansa bile backend bilgisi yoksa (connection pooling, HTTP/2 vb.) bloker oluyorsunuz — fundamental bilgi hâlâ kritik.
- **Single founder artışı:** Agent team'leriyle tek kişi büyük projeler çıkarabiliyor; takım büyüdükçe iletişim overhead'i bazen işi yavaşlatıyor.
- **Abstraction katmanları:** Assembly → C → Python → Framework → Doğal dil. Her geçişte "eski dili bilenler" endişe yaşadı. Şimdi de aynısı oluyor.
- **"Taste" kavramı:** Konferansta öne çıkan yeni bir kavram — sentaks değil "zevk sahibi olmak", kaliteyi görebilmek, doğru kombinasyonu seçebilmek artık kritik beceri.

---

*Bu özet transkripsiyon içeriğine dayanmaktadır. Tüm slayt başlıkları için eğitimcinin söyledikleri baz alınmıştır.*
