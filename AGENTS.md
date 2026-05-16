# AGENTS.md — Repository Guidelines

## ZORUNLU KURAL: Bu Dosyaları Her Zaman Güncelle

**Her kod değişikliğinin ardından, commit yapmadan önce `CLAUDE.md` ve `AGENTS.md` dosyalarını güncellemelisin.**

Aşağıdaki durumlarda ilgili bölümleri güncelle:

| Değişiklik | Güncelle |
|---|---|
| Yeni modül / dosya eklendi | "Proje Yapısı" bölümü her iki dosyada |
| Yeni API endpoint'i | `CLAUDE.md` endpoint tablosu + bu dosyadaki routing bölümü |
| Yeni frontend sayfası | `CLAUDE.md` mimari tablosu + bu dosyadaki yapı bölümü |
| Yeni `pip` bağımlılığı | Bu dosyadaki bağımlılıklar bölümü |
| Yeni ortam değişkeni | Her iki dosyadaki ilgili notlar |

Bu dosyaları güncellemeden commit atmak yasaktır.

---

## Proje Yapısı

```
app.py                  # Flask uygulaması; routing, doğrulama, oturum yönetimi
llm.py                  # OpenAI istemcisi; hafızasız stream_llm() fonksiyonu
asistan.py              # Asistan sınıfı; conversation history + stream_sohbet()
agent.py                # Agent sınıfı; tool-calling agentic loop + calistir() generator
backend/
  __init__.py           # Backend package işaretçisi
  tools/
    __init__.py         # Agent TOOL_DEFINITIONS ve TOOL_FUNCTIONS registry'si
    text_analyzer.py    # analyze_text aracı; metin istatistikleri üretir
frontend/
  index.html            # LLM arayüzü: tek seferlik prompt/yanıt sayfası
  asistan.html          # Asistan arayüzü: çok turlu, baloncuklu sohbet sayfası
  agent.html            # Agent arayüzü: tool call'ları ve adımları görsel gösterim
tests/
  test_agent_tool_execution.py  # Agent tool-call akışını sahte OpenAI yanıtlarıyla test eder
  test_app_validation.py        # Flask validation davranışlarını test eder
  test_text_analyzer_tool.py    # analyze_text ve registry testleri
requirements.txt        # Python bağımlılıkları
.env                    # Yerel sırlar (commit edilmez); OPENAI_API_KEY buraya
CLAUDE.md               # Claude Code'a mimari rehberlik
AGENTS.md               # Bu dosya; geliştirici ve ajan kuralları
```

Backend routing ve doğrulama `app.py`'de kalır. Provider'a özgü LLM çağrıları `llm.py`, `asistan.py` veya `agent.py`'de kalır. Agent tool'ları `backend/tools/` altında ayrı dosyalara eklenir ve `backend/tools/__init__.py` içindeki `TOOL_DEFINITIONS` ile `TOOL_FUNCTIONS` registry'lerine kaydedilir. Statik dosyalar `frontend/` altına eklenir.

---

## API Endpoint'leri

| Method | Path | Body | Açıklama |
|---|---|---|---|
| POST | `/api/chat` | `{model, system_instructions, user_prompt}` | Hafızasız, tek seferlik LLM çağrısı (streaming, text/plain) |
| POST | `/api/asistan/yeni` | `{model, system_instructions}` | Yeni asistan oturumu oluşturur, `session_id` döner |
| POST | `/api/asistan/sohbet` | `{session_id, user_prompt}` | Asistana mesaj gönderir (streaming, text/plain) |
| POST | `/api/agent/yeni` | `{model, system_instructions}` | Yeni agent oturumu oluşturur, `session_id` döner |
| POST | `/api/agent/calistir` | `{session_id, user_prompt}` | Agent'ı çalıştırır (NDJSON stream; event tipleri: `step_start`, `thinking`, `tool_call`, `tool_result`, `text`, `done`, `error`) |

---

## Geliştirme Komutları

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug   # http://127.0.0.1:5000
python3 -m pytest
```

---

## Bağımlılıklar

- `flask`: Backend routing ve HTTP response streaming.
- `openai`: LLM ve tool-calling API istemcisi.
- `python-dotenv`: Yerel `.env` dosyasından `OPENAI_API_KEY` yükleme.
- `pytest`: Otomatik test suite.

---

## Kod Stili

- Python 3, 4 boşluk girinti, yeniden kullanılabilir yardımcılar için type hint.
- `stream_llm(...) -> Iterator[str]` ve `stream_sohbet(...) -> Iterator[str]` imzası örnek alınmalı.
- Hata mesajları API sınırını geçiyorsa kullanıcıya yönelik, provider hatası gizlenmeli.
- Frontend: sade HTML/CSS/JS, `camelCase` JS değişkenleri, amaca uygun `id` isimleri.

---

## Test Kılavuzu

Otomatik test suite `tests/` altında mevcuttur:

- Yeni testleri `tests/` altında, `test_*.py` adlandırmasıyla ekle.
- `pytest` kullan; gerçek OpenAI çağrılarını testlerde mock/fake nesnelerle izole et.
- Öncelikli test alanları: Flask route doğrulama, `ALLOWED_MODELS` kontrolü, streaming hata yönetimi, asistan history doğruluğu ve agent tool registry entegrasyonu.

```sh
pytest
```

Frontend değişikliklerinde tarayıcıda şunları manuel doğrula: boş prompt engelleme, model seçimi, streaming render, asistan history sürekliliği.

---

## Commit ve PR Kuralları

- Commit mesajları kısa ve imperative: `Add streaming assistant`, `Validate chat payload`.
- PR'lara: kısa özet, test notları, gerekli `.env` değişiklikleri, UI değişimi varsa ekran görüntüsü ekle.

---

## Güvenlik

- API anahtarları yalnızca `.env`'de; `python-dotenv` ile yükle. Commit etme.
- Log veya API yanıtında sır basmak yasak.
- `ALLOWED_MODELS` değiştiğinde `app.py` ve tüm frontend `<select>` elementleri birlikte güncellenmeli.
- `_asistanlar` dict'i sunucu hafızasında; production için kalıcı depolama gerekir.
