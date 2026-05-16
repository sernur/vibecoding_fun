import json
import re

WORD_PATTERN = re.compile(
    r"[A-Za-zÇĞİÖŞÜçğıöşü0-9]+(?:['’-][A-Za-zÇĞİÖŞÜçğıöşü0-9]+)?"
)


def analyze_text(text: str) -> str:
    """Return basic Turkish-friendly statistics for the given text."""
    if not isinstance(text, str):
        return "Hata: text alanı metin olmalıdır."

    stripped_text = text.strip()
    words = WORD_PATTERN.findall(stripped_text)
    sentence_count = _count_sentences(stripped_text)
    character_count = len(text)
    character_count_without_spaces = sum(1 for char in text if not char.isspace())
    average_word_length = (
        round(sum(len(word) for word in words) / len(words), 2)
        if words
        else 0
    )
    longest_word = max(words, key=len) if words else ""

    result = {
        "kelime_sayisi": len(words),
        "cumle_sayisi": sentence_count,
        "karakter_sayisi": character_count,
        "bosluksuz_karakter_sayisi": character_count_without_spaces,
        "ortalama_kelime_uzunlugu": average_word_length,
        "en_uzun_kelime": longest_word,
    }
    return json.dumps(result, ensure_ascii=False)


def _count_sentences(text: str) -> int:
    if not text:
        return 0

    sentences = [part.strip() for part in re.split(r"[.!?]+", text) if part.strip()]
    return len(sentences) if sentences else 1
