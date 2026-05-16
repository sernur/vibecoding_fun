import json
import os
from types import SimpleNamespace

os.environ.setdefault("OPENAI_API_KEY", "test-key")

import agent
from agent import Agent, TOOLS


def _message(content=None, tool_calls=None):
    return SimpleNamespace(content=content, tool_calls=tool_calls)


def _tool_call(name, arguments, call_id="call_1"):
    return SimpleNamespace(
        id=call_id,
        function=SimpleNamespace(name=name, arguments=json.dumps(arguments)),
    )


def _response(message):
    return SimpleNamespace(choices=[SimpleNamespace(message=message)])


def test_agent_exposes_analyze_text_tool_definition():
    tool_names = {
        tool["function"]["name"]
        for tool in TOOLS
    }

    assert "analyze_text" in tool_names


def test_agent_runs_analyze_text_tool_and_continues_conversation(monkeypatch):
    responses = iter([
        _response(_message(
            tool_calls=[
                _tool_call("analyze_text", {"text": "Bir iki üç. Dört beş!"}),
            ],
        )),
        _response(_message(content="Metinde 5 kelime ve 2 cümle var.")),
    ])

    def fake_create(**kwargs):
        assert kwargs["tool_choice"] == "auto"
        return next(responses)

    monkeypatch.setattr(agent.client.chat.completions, "create", fake_create)

    events = list(
        Agent("Araçları kullan.", "gpt-4.1-mini").calistir("Metni analiz et.")
    )

    assert {
        "type": "tool_call",
        "name": "analyze_text",
        "args": {"text": "Bir iki üç. Dört beş!"},
    } in events
    tool_result = next(event for event in events if event["type"] == "tool_result")
    parsed_result = json.loads(tool_result["result"])
    assert parsed_result["kelime_sayisi"] == 5
    assert parsed_result["cumle_sayisi"] == 2
    assert events[-2] == {"type": "text", "content": "Metinde 5 kelime ve 2 cümle var."}
    assert events[-1] == {"type": "done"}
