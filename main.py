from flask import Flask
from flask_cors import CORS
from router import vizitka
from settings import settings
from tg_bot.bot import start_bot
import threading
import asyncio
app = Flask(__name__)
CORS(app)
app.register_blueprint(vizitka)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

async def main():
    # Запускаем Flask в отдельном потоке
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Запускаем Telegram бота
    await start_bot()

if __name__ == "__main__":
    asyncio.run(main())