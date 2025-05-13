from flask import Blueprint, request, jsonify
from settings import settings
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

vizitka = Blueprint("vizitka", __name__)


async def send_to_telegram(name: str, message: str, number: str):
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    text = (
        f"📩 Новое сообщение с сайта:\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Телефон: {number}\n"
        f"✉️ Сообщение: {message}"
    )
    await bot.send_message(chat_id=settings.CHAT_ID, text=text)
    await bot.session.close()


@vizitka.route("/", methods=["POST"])
def get_data():
    data = request.json
    name = data.get("name")
    message = data.get("message")
    number = data.get("number")

    if not name or not message or not number:
        return jsonify({"error": "Missing parameter name or message or number"}), 400

    try:
        asyncio.run(send_to_telegram(name, message, number))
        return jsonify({"status": "Message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500