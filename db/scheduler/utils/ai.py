# Заглушка под ИИ-интеграцию
# В будущем сюда можно подключить OpenAI, Groq или другие LLM

def process_ai_query(user_text: str) -> str:
    # Пока просто возвращает то, что получил
    return f"Вы задали: {user_text}"
