import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = {
    int(user_id)
    for user_id in os.getenv("ADMIN_IDS", "").split(",") if user_id.strip()
}

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

if not ADMIN_IDS:
    raise ValueError("ADMIN_IDS is missing!")