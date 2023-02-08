"""Главный файл проекта. Через него запускается бот."""

from aiogram.utils import executor

from create_bot import dp
from handlers import aiogam_handlers
from handlers import admin_aiogram_handlers


async def on_startup(_):
    print('Бот вышел в онлайн.')

aiogam_handlers.register_handlers(dp)
admin_aiogram_handlers.register_admin_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
