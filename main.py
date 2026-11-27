
import os
import hmac

from fastapi import FastAPI, Request, HTTPException
from aiogram import Bot
from aiogram.types import Update

from config import BOT_TOKEN
from bot import dp


app = FastAPI()

bot = Bot(token=BOT_TOKEN)

WEBHOOK_SECRET = os.environ["WEBHOOK_SECRET"]


@app.get("/")
async def home():
    return {
        "message": "Course Bot is running!"
    }


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):

    # Verify Telegram webhook secret
    received_secret = request.headers.get(
        "X-Telegram-Bot-Api-Secret-Token", ""
    )

    if not hmac.compare_digest(
        received_secret,
        WEBHOOK_SECRET
    ):
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

    # Read Telegram update
    data = await request.json()

    update = Update.model_validate(
        data,
        context={"bot": bot}
    )

    # Process Telegram update
    await dp.feed_update(bot, update)

    return {"ok": True}
