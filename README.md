# FastAPI-Telegram

FastAPI project template that uses Telegram Login Widget for authentication.

## Instalation

1. Create `.env` file based on the `.env.example` file's structure.
2. Add your bot's token and your app's secret key there.
3. The project is ready to be launched with `docker compose up` command.
4. Do not forget to run migrations when everything is up and running.

## Usage

- Just point your frontend Telegram login widget to `/api/v1/auth/telegram/callback` endpoint and you are ready to go.
