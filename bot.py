"""
bot.py — Telegram bot entry point.

Run with:  python bot.py   (from inside the experiment/ folder)

This file only wires up the Telegram Application and starts polling.
All actual logic lives in handlers/ — nothing here should need to change
when business logic changes.
"""

import logging
from datetime import time as dt_time

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import ISRAEL_TZ, TELEGRAM_BOT_TOKEN
from handlers.callbacks import handle_callback
from handlers.commands import (
    tg_balance,
    tg_categories,
    tg_category,
    tg_delete,
    tg_help,
    tg_keywords,
    tg_summary,
)
from handlers.message import tg_handle_message
from handlers.monthly_report import send_monthly_report, tg_test_report

logging.basicConfig(
    format="%(asctime)s  %(levelname)s  %(name)s  %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def _post_init(application: Application) -> None:
    """Register scheduled jobs after the Application is fully initialised."""
    application.job_queue.run_monthly(
        send_monthly_report,
        when=dt_time(hour=9, minute=0, second=0, tzinfo=ISRAEL_TZ),
        day=1,
    )
    logger.info("Monthly report job registered: 1st of each month at 09:00 IST")


def create_app() -> Application:
    if not TELEGRAM_BOT_TOKEN:
        raise EnvironmentError("TELEGRAM_BOT_TOKEN is not set in .env")

    app = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .post_init(_post_init)
        .build()
    )

    # Slash commands
    app.add_handler(CommandHandler("start",      tg_help))
    app.add_handler(CommandHandler("help",       tg_help))
    app.add_handler(CommandHandler("categories", tg_categories))
    app.add_handler(CommandHandler("keywords",   tg_keywords))
    app.add_handler(CommandHandler("summary",    tg_summary))
    app.add_handler(CommandHandler("category",   tg_category))
    app.add_handler(CommandHandler("balance",    tg_balance))
    app.add_handler(CommandHandler("delete",      tg_delete))
    app.add_handler(CommandHandler("report", tg_test_report))

    # Inline button callbacks (fuzzy confirm yes/no)
    app.add_handler(CallbackQueryHandler(handle_callback))

    # Free-text messages — must be registered last
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, tg_handle_message))

    return app


if __name__ == "__main__":
    logger.info("Starting bot...")
    create_app().run_polling()
