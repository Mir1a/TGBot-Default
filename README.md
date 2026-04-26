# Portfolio Telegram Bot

A simple informational Telegram bot for a developer portfolio. Built with **FastAPI** + **python-telegram-bot** using webhooks. Supports **Ukrainian** and **English** languages.

---

## About the Bot

The bot does not perform any actions — it only provides information about the developer and their stack through a convenient button menu. On first launch, the user selects a language; the preference is stored in a SQLite database.

**Buttons:**
- `🤖 About me` — bot description and technologies
- `👤 About my creator` — information about the developer
- `📞 Contacts` — GitHub and LinkedIn
- `🛠 Stack` — technology stack

---

## Stack

- **Python 3.11+**
- **FastAPI** — web server, receives webhooks from Telegram
- **python-telegram-bot** — Telegram API integration
- **SQLAlchemy + aiosqlite** — async SQLite for user language preferences
- **Docker** — containerization
- **uv** — dependency management

---

## Project Structure

```
app/
├── main.py               # FastAPI app, lifespan, webhook registration
├── config.py             # Settings from .env
├── db/
│   ├── __init__.py       # get_user_language / set_user_language helpers
│   ├── models.py         # SQLAlchemy User model
│   └── session.py        # Async engine, session factory, init_db()
├── api/
│   ├── router.py         # POST /webhook, GET /health
│   └── service.py        # Processes Telegram Update
└── bot/
    ├── __init__.py        # BUTTONS dict (bilingual button labels)
    ├── application.py     # Bot singleton, handler registration
    ├── keyboards.py       # ReplyKeyboard, InlineKeyboard, language keyboard
    ├── texts.py           # Bilingual message texts (MarkdownV2)
    └── handlers/
        ├── start.py       # /start — language selection or main menu
        ├── language.py    # Callback handler for language choice
        └── message.py     # Button routing with language awareness
```

---

## Setup

### Local

```bash
cp .env.example .env
# Fill in TOKEN in .env

make install
make run
```

### Docker

```bash
cp .env.example .env
# Fill in TOKEN and WEBHOOK_URL in .env

make docker-up
```

---

## Configuration

`.env` file:

```env
TOKEN=your_telegram_bot_token_here
WEBHOOK_URL=https://yourdomain.com/webhook
```

| Variable | Description |
|----------|-------------|
| `TOKEN` | Bot token from @BotFather |
| `WEBHOOK_URL` | Public HTTPS URL for the webhook |

> For local development you can use [ngrok](https://ngrok.com): `ngrok http 8000`

---

## Make Commands

| Command | Action |
|---------|--------|
| `make install` | Install dependencies |
| `make run` | Run locally with hot-reload |
| `make docker-up` | Build and start Docker |
| `make docker-up-detached` | Start Docker in background |
| `make docker-down` | Stop Docker |
| `make black` | Format code |
| `make flake8` | Check code style |
| `make mypy` | Check types |
| `make requirements` | Update requirements.txt |

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/webhook` | Receives updates from Telegram |
| `GET` | `/health` | Server health check |

---

## Contacts

- GitHub: [github.com/Mir1a](https://github.com/Mir1a)
- LinkedIn: [linkedin.com/in/matvey-bliznyuk-a735ab303](https://www.linkedin.com/in/matvey-bliznyuk-a735ab303/)
