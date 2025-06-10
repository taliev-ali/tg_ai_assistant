import asyncio
from aiogram import Bot

# Пример: напоминание через 1 минуту (в будущем сделаем гибко)
def schedule_task(bot: Bot, user_id: int, task_text: str):
    async def remind():
        await asyncio.sleep(60)  # ⏱️ 60 секунд — потом напомнит
        await bot.send_message(user_id, f"🔔 Напоминание: {task_text}")

    loop = asyncio.get_event_loop()
    loop.create_task(remind())
