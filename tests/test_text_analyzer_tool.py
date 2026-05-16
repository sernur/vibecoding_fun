import json

from backend.tools import TOOL_DEFINITIONS, TOOL_FUNCTIONS
from backend.tools.text_analyzer import analyze_text


def test_analyze_text_returns_expected_statistics_for_turkish_text():
    result = json.loads(analyze_text("Merhaba dünya! Bugün hava çok güzel."))

    assert result == {
        "kelime_sayisi": 6,
        "cumle_sayisi": 2,
        "karakter_sayisi": 36,
        "bosluksuz_karakter_sayisi": 31,
        "ortalama_kelime_uzunlugu": 4.83,
        "en_uzun_kelime": "Merhaba",
    }


def test_analyze_text_handles_empty_text():
    result = json.loads(analyze_text("   "))

    assert result["kelime_sayisi"] == 0
    assert result["cumle_sayisi"] == 0
    assert result["en_uzun_kelime"] == ""


def test_text_analyzer_is_registered_for_agent_tool_calling():
    tool_names = {
        tool["function"]["name"]
        for tool in TOOL_DEFINITIONS
    }

    assert "analyze_text" in tool_names
    assert "analyze_text" in TOOL_FUNCTIONS
    assert "kelime_sayisi" in TOOL_FUNCTIONS["analyze_text"]({"text": "iki kelime"})
