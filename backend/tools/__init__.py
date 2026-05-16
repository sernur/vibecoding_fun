from collections.abc import Callable

from .text_analyzer import analyze_text

ToolFunction = Callable[[dict], str]

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "analyze_text",
            "description": (
                "Verilen metin için kelime, cümle, karakter, boşluksuz karakter, "
                "ortalama kelime uzunluğu ve en uzun kelime istatistiklerini döndürür."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Analiz edilecek metin.",
                    },
                },
                "required": ["text"],
                "additionalProperties": False,
            },
        },
    }
]

TOOL_FUNCTIONS: dict[str, ToolFunction] = {
    "analyze_text": lambda args: analyze_text(args.get("text", "")),
}
