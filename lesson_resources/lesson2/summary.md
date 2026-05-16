# Ders 2 Özeti — Claude Code ile Canlı Kodlama

**Süre:** ~2 saat 30 dakika  
**Konu:** Claude Code ve Codex ile sıfırdan Flask + LLM uygulaması geliştirmek

---

## Genel Bakış

Bu derste Claude Code terminal arayüzü canlı olarak kullanılarak, öğrencilerle birlikte sıfırdan bir web uygulaması inşa edildi. Uygulama kademeli olarak büyütüldü: önce hafızasız tek seferlik LLM çağrısı, ardından streaming, sonra conversation history tutan asistan, en son olarak tool-calling yapabilen bir kodlama agenti eklendi.

---

## Araçlar ve Ortam

### Claude Code vs Cursor vs Codex
- **Claude Code**: Terminal tabanlı CLI; Mac ve Linux'ta kolay kurulum, Windows'ta bazı farklılıklar var.
- **Cursor**: IDE/kod editörü; görsel arayüz ile dosya gezintisi ve diff görüntüleme daha rahat.
- **Codex (OpenAI)**: Claude Code'a benzer agentic CLI; `resume` ile önceki session'a geri dönme ve `review` komutu gibi kendine özgü özellikleri var.

Hoca tercihen Claude Code terminalini kullandı; gerektiğinde Codex ile cross-review yaptı.

---

## Claude Code'da Öğrenilen Özellikler

| Özellik | Nasıl Kullanılır |
|---|---|
| Mod değiştirme | `Shift+Tab` — Accept Edits / Plan Modu |
| İptal etme | 2× `Escape` (Claude), `Ctrl+C` (Codex) |
| Dosya mention | `@dosyaadi` ile dosyayı bağlama ekle |
| Çok satırlı giriş | `Ctrl+G` ile editör açılır |
| Ses ile komut | `Space` basılı tut, Türkçe konuş |
| Permission yönetimi | `/permissions` veya global settings'te "Skip Permissions" |
| Config | `/config` — dil, model, renk vb. ayarlar |
| Alias | `.zshrc`/`.bashrc`'ye `alias c='claude'` tanımlanabilir |

---

## Projenin Gelişim Aşamaları

### Aşama 1 — Hafızasız LLM Arayüzü (`/`)
Claude Code'a `llm.py` dosyasını oluşturması söylendi: OpenAI SDK kullanılarak `stream_llm()` fonksiyonu yazıldı. Aynı anda `frontend/index.html` ile model seçimi (combo box), system instructions ve prompt giriş alanı içeren basit bir sayfa üretildi. Flask ile `/api/chat` endpoint'i tanımlandı.

**Önemli not:** Önce `git init` yapılmadığı fark edildi; git'in vibe coding'de kritik önemi vurgulandı — her prompt sonrası test + commit alışkanlığı kazandırıldı.

### Aşama 2 — Streaming
İlk arayüz cevabı tek seferde döndürüyordu. `stream=True` parametresi eklenerek ChatGPT tarzı gerçek zamanlı çıktı sağlandı. Flask tarafında `stream_with_context()` + `text/plain` streaming kullanıldı; frontend `ReadableStream` ile chunk'ları okudu.

Codex'e bu değişiklik yaptırıldı, ardından Claude Opus ile cross-review yapıldı. Claude şunları buldu:
- Eski `call_llm` fonksiyonu ölü kod haline geldi
- Model doğrulaması eksik
- Hata yönetimi yok

Bulgular Codex'e gönderilerek düzeltmeler yaptırıldı; `ALLOWED_MODELS` set'i ve try/except blokları eklendi.

### Aşama 3 — Asistan (`/asistan`)
`asistan.py` dosyasında `Asistan` sınıfı oluşturuldu. **LLM'den tek farkı:** `self.history` listesi — her soru/cevap çifti bu listeye ekleniyor, sonraki çağrıda modele tekrar gönderiliyor. Bu sayede "hafıza" sağlanıyor.

Session yönetimi için `/api/asistan/yeni` → `session_id` döner; `/api/asistan/sohbet` o session'a mesaj gönderir. Server hafızasında `_asistanlar` dict'i oturumları tutar (sunucu restart'ta sıfırlanır).

Sohbet baloncuklu arayüz olarak `frontend/asistan.html`'de gösterildi.

### Aşama 4 — Kodlama Agenti (`/agent`)
`agent.py` dosyasında `Agent` sınıfı oluşturuldu. **Asistandan tek farkı:** tool-calling desteği.

**Agent'ın sahip olduğu tool'lar:**
- `terminal` — `/tmp/agent_workspace` dizininde `subprocess` ile shell komutu çalıştırır
- `dosya_oku` — dosya içeriğini okur
- `dosya_yaz` — dosya oluşturur/üzerine yazar

**Agent loop mantığı:**
1. User prompt'u history'ye ekle
2. Model + tool listesini OpenAI'ye gönder
3. Model tool_call dönerse → tool'u çalıştır, sonucu history'ye ekle → 2'ye dön
4. Model düz metin dönerse → bitir

`calistir()` bir generator'dür; her adımda `step_start`, `thinking`, `tool_call`, `tool_result`, `text`, `done` event'leri yield eder. Frontend NDJSON formatındaki bu event'leri görsel bloklara dönüştürür.

---

## Kritik Kavramlar

### Prompt Engineering — Boyacı Analojisi
Model büyüklüğü ile prompt detayı arasındaki ilişki şöyle açıklandı:
- Yeni başlayan boyacı = küçük model (gpt-4.1-mini)
- Deneyimli usta = büyük model (gpt-4o / Opus)
- Detaysız komut → generic sonuç; detaylı komut → büyük model gerektir

Kolay görevler için küçük model yeterli; karmaşık, multi-step görevler için büyük model + thinking.

### CLAUDE.md ve AGENTS.md
- `/init` komutu projeyi tarayıp bu dosyaları oluşturur.
- Claude her komutta `CLAUDE.md`'yi okur; Codex her komutta `AGENTS.md`'yi okur.
- Bu dosyalar projenin "hafızası" — yoksa model her seferinde projeyi baştan tarar (token israfı).
- Dosyaya "her değişiklikten önce bunu güncelle" kuralı eklenerek dosyanın güncel kalması sağlandı.
- Çok büyük olmamasına dikkat edilmeli; model kendisi uyarıyor.

### Context Yönetimi
- Her görev tamamlandığında context temizlenmeli (`/clear`) → token verimliliği ve performans.
- Büyük projelerde git commit'leri doğal bir hafıza oluşturur; model'e "son 10 commit'i oku" denilebilir.
- Spec ve plan dökümanları git repo'sunda markdown veya git issues olarak tutulabilir.

### Plan Modu
- `Shift+Tab` iki kez basılarak plan moduna geçilir.
- Bu modda model **sadece plan yapar, dosyalara dokunmaz**.
- Büyük özellikler için önerilen akış: Spec → Plan (review et) → Implement → Test → PR.

### Cross-Review Stratejisi
Codex'e yazdırılan kodu Claude'a, Claude'a yazdırılanı Codex'e review ettirmek; ya da aynı modelin farklı session'larını (Sonnet + Opus) kullanmak kaliteyi artırıyor.

---

## Mimari Özet (Ders Sonunda Oluşturulan Proje)

```
vbl1/
├── app.py          # Flask routing + session yönetimi
├── llm.py          # OpenAI client + stream_llm()
├── asistan.py      # Asistan sınıfı (conversation history)
├── agent.py        # Agent sınıfı (tool-calling loop)
├── frontend/
│   ├── index.html  # Hafızasız LLM arayüzü
│   ├── asistan.html# Baloncuklu sohbet arayüzü
│   └── agent.html  # Adım adım agent arayüzü (NDJSON stream)
├── .env            # OPENAI_API_KEY (gitignore'da)
├── .gitignore
├── requirements.txt
└── CLAUDE.md
```

**Streaming formatları:**
- LLM ve Asistan → `text/plain` stream
- Agent → `application/x-ndjson` (satır satır JSON event'leri)

---

## Ödev

Repoyu fork edin; coding agent'ın yerine **farklı bir domain** (seyahat, yemek, eğitim vb.) seçin ve agent'a yeni tool'lar ekleyin. Sonucu GitHub'a koyup repo linkini paylaşın.

---

## Notlar ve Sorular

- **Türkçe vs İngilizce:** Token farkı önemsiz; kalite farkı günümüz modellerinde minimal.
- **Anthropic'in yeni araştırması:** Model iç aktivasyonlarının (nöron-seviye düşünme süreci) izlenebilir hale getirilmesi duyuruldu.
- **Bir sonraki ders:** Git worktree, branch bazlı geliştirme, paralel feature geliştirme, PR süreçleri.
