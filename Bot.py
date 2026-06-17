from telegram import Bot
from datetime import datetime, timedelta
import os
import asyncio

TOKEN = os.environ["BOT_TOKEN"]
GROUP_ID = os.environ["GROUP_ID"]

async def main():
    bot = Bot(token=TOKEN)

    today = datetime.now()

    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7

    monday = today + timedelta(days=days_until_monday)

    poll = await bot.send_poll(
        chat_id=GROUP_ID,
        question=f"Графік на тиждень з {monday.strftime('%d.%m.%Y')}",
        options=[
            "Працюю",
            "Вихідний",
            "Потрібна заміна"
        ],
        is_anonymous=False
    )

    await bot.pin_chat_message(
        chat_id=GROUP_ID,
        message_id=poll.message_id
    )

asyncio.run(main())
