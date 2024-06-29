# FastAPI-Telegram

<img src="https://github.com/dabarov/fastapi-telegram/assets/36531464/5bc2a850-481c-42f1-a99c-6ea13a84fd69" align="right" alt="FastAPI-Telegram" width="150" height="150">

A FastAPI project template with Telegram authentication that:
- Uses the Telegram Login Widget for authentication.
- Demonstrates how to send messages to the current user.
- Uses PostgreSQL to store user data.
- Uses Ruff for linting and formatting.
- Is Dockerized.

## Using the Template

You can start by either:

- Clicking on the **Use this template** button and selecting **Create a new repository**.

    <img src="https://docs.github.com/assets/cb-76823/mw-1440/images/help/repository/use-this-template-button.webp" alt="Use this template" width="400">

OR 

- Directly cloning this repository:

    ```sh
    git clone https://github.com/dabarov/fastapi-telegram.git
    ```

## Instalation

For direct installation and usage:

1. Create a `.env` file based on the structure of the `.env.example` file.
2. Install the Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run migrations after setting the database variables in `.env`:

    ```sh
    alembic upgrade head
    ```

4. Launch your app with the following command:

    ```sh
    uvicorn app.main:app --port 8000 --reload
    ```

Alternatively, you can run the application in a Dockerized environment with the following command:

```sh
docker-compose -f compose.dev.yml up
```    

## Usage

### Adding to Your Frontend Application

- Add the Telegram Login Widget to your frontend based on [this article](https://core.telegram.org/widgets/login).
- Point the `data-auth-url` to the `/api/v1/auth/telegram/callback` endpoint.

### Available Endpoints

The routes are available in the `app/api/routes` directory.

There are two endpoints for authentication (`app/api/routes/auth.py`):  
- `GET /api/v1/auth/telegram/callback` handles the callback from the Telegram Login Widget.
- `GET /api/v1/auth/logout` removes authentication for the user.

There are two endpoints to demonstrate the usage of the current user's data (`app/api/routes/user.py`):
- `GET /api/v1/telegram/user/avatar` redirects to the current user's avatar image.
- `POST /api/v1/telegram/send-message` sends a text message from the request body's `message` field to the current user.

### Available FastAPI Dependencies

The dependencies are available in `app/api/deps.py`:

- `SessionDep` for the database session.
- `CurrentUserDep` for current user data from the database.
- `TelegramBotDep` provides the Telegram bot object of type `Bot` for sending messages, etc.
  