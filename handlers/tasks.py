from aiogram import Dispatcher, types
from db.database import get_tasks

def register_task_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['tasks'])
    async def list_tasks(message: types.Message):
        tasks = get_tasks(message.from_user.id)
        if not tasks:
            await message.reply("У тебя нет сохранённых задач.")
        else:
            reply = "\n".join([f"• {task[0]}" for task in tasks])
            await message.reply(f"Твои задачи:\n{reply}")
