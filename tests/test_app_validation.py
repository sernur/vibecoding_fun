import os

os.environ.setdefault("OPENAI_API_KEY", "test-key")

from app import app


def test_chat_rejects_empty_prompt_before_calling_model():
    client = app.test_client()

    response = client.post("/api/chat", json={
        "model": "gpt-4.1-mini",
        "user_prompt": "   ",
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "user_prompt bos olamaz"


def test_agent_session_rejects_invalid_model():
    client = app.test_client()

    response = client.post("/api/agent/yeni", json={
        "model": "not-a-real-model",
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Geçersiz model"
