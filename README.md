# Portfolio Telegram Bot

Простий інформаційний Telegram-бот для портфоліо. Реалізований на **FastAPI** + **python-telegram-bot** з вебхуком.

## Про бота

Бот не виконує жодних дій - він лише надає інформацію про розробника та його стек через зручне меню з кнопками.

**Кнопки:**
- `🤖 Про мене` - опис бота та технологій
- `👤 Про мого творця` - інформація про розробника
- `📞 Контактні дані` - GitHub та LinkedIn
- `🛠 Стек` - технологічний стек

## Стек

- **Python 3.11+**
- **FastAPI** - вебсервер, приймає вебхуки від Telegram
- **python-telegram-bot** - робота з Telegram API
- **Docker** - контейнеризація
- **uv** - управління залежностями

## Структура проєкту

```
app/
├── main.py               # FastAPI застосунок, lifespan, реєстрація вебхука
├── config.py             # Налаштування з .env
├── api/
│   ├── router.py         # POST /webhook, GET /health
│   └── service.py        # Обробка Update від Telegram
└── bot/
    ├── __init__.py        # Enum Btn з назвами кнопок
    ├── application.py     # Синглтон бота, реєстрація хендлерів
    ├── keyboards.py       # ReplyKeyboard та InlineKeyboard
    ├── texts.py           # Тексти повідомлень (MarkdownV2)
    └── handlers/
        ├── start.py       # /start
        └── message.py     # Роутинг кнопок через match/case
```

## Запуск

### Локально

```bash
cp .env.example .env
# Заповнити TOKEN у .env

make install
make run
```

### Docker

```bash
cp .env.example .env
# Заповнити TOKEN та WEBHOOK_URL у .env

make docker-up
```

## Налаштування

Файл `.env`:

```env
TOKEN=your_telegram_bot_token_here
WEBHOOK_URL=https://yourdomain.com/webhook
```

| Змінна | Опис |
|--------|------|
| `TOKEN` | Токен бота від @BotFather |
| `WEBHOOK_URL` | Публічний HTTPS URL для вебхука |

> Для локальної розробки можна використати [ngrok](https://ngrok.com): `ngrok http 8000`

## Команди Make

| Команда | Дія |
|---------|-----|
| `make install` | Встановити залежності |
| `make run` | Запустити локально з hot-reload |
| `make docker-up` | Зібрати та запустити Docker |
| `make docker-up-detached` | Запустити Docker у фоні |
| `make docker-down` | Зупинити Docker |
| `make black` | Форматування коду |
| `make flake8` | Перевірка стилю |
| `make mypy` | Перевірка типів |
| `make requirements` | Оновити requirements.txt |

## Ендпоінти

| Метод | Шлях | Опис |
|-------|------|------|
| `POST` | `/webhook` | Приймає апдейти від Telegram |
| `GET` | `/health` | Перевірка стану сервера |

## Контакти

- GitHub: [github.com/Mir1a](https://github.com/Mir1a)
- LinkedIn: [linkedin.com/in/matvey-bliznyuk-a735ab303](https://www.linkedin.com/in/matvey-bliznyuk-a735ab303/)
