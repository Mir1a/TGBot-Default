TEXTS: dict[str, dict[str, str]] = {
    "uk": {
        "welcome": (
            "Привіт\\! 👋\n\n"
            "Я \\- портфоліо\\-бот Матвія, Python розробника\\.\n\n"
            "Оберіть розділ за допомогою кнопок нижче:"
        ),
        "about_bot": (
            "🤖 *Про мене*\n\n"
            "Цей бот створений як портфоліо\\-проєкт для демонстрації навичок розробки\\.\n\n"
            "Це простий інформаційний бот \\- він лише надає інформацію та не виконує жодних дій\\.\n\n"
            "Реалізований з використанням *FastAPI* \\+ *python\\-telegram\\-bot*\\."
        ),
        "about_me": (
            "👤 *Про мого творця*\n\n"
            "Мене звати *Матвій*, працюю Python розробником з 2023 року\\.\n\n"
            "Пишу на Python\\. Люблю вивчати нове та пробувати себе в різному\\.\n\n"
            "Цей TG бот \\- один із моїх проєктів\\."
        ),
        "contacts": "📞 *Контактні дані*\n\nНатисніть на кнопку нижче, щоб перейти:",
        "stack": (
            "🛠 *Стек технологій*\n\n"
            "Python \\| Django \\| FastAPI \\| PostgreSQL \\| Docker\n"
            "REST API \\| Celery \\| Celery Scheduler\n"
            "Alembic \\| SQLAlchemy \\| Pydantic"
        ),
        "unknown": "Використовуйте кнопки меню нижче:",
    },
    "en": {
        "welcome": (
            "Hello\\! 👋\n\n"
            "I'm Matvii's portfolio bot, a Python developer\\.\n\n"
            "Choose a section using the buttons below:"
        ),
        "about_bot": (
            "🤖 *About me*\n\n"
            "This bot was created as a portfolio project to showcase development skills\\.\n\n"
            "It's a simple informational bot \\- it only provides information and performs no actions\\.\n\n"
            "Built with *FastAPI* \\+ *python\\-telegram\\-bot*\\."
        ),
        "about_me": (
            "👤 *About my creator*\n\n"
            "My name is *Matvii*, I've been working as a Python developer since 2023\\.\n\n"
            "I write in Python\\. I love learning new things and trying myself in different areas\\.\n\n"
            "This Telegram bot is one of my projects\\."
        ),
        "contacts": "📞 *Contacts*\n\nClick the button below to proceed:",
        "stack": (
            "🛠 *Tech Stack*\n\n"
            "Python \\| Django \\| FastAPI \\| PostgreSQL \\| Docker\n"
            "REST API \\| Celery \\| Celery Scheduler\n"
            "Alembic \\| SQLAlchemy \\| Pydantic"
        ),
        "unknown": "Please use the menu buttons below:",
    },
}


def get_text(lang: str, key: str) -> str:
    return TEXTS.get(lang, TEXTS["uk"])[key]
