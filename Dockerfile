FROM python:3.12.3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./.env /app/.env
COPY ./alembic.docker.ini /app/alembic.ini
COPY ./ruff.toml /app/ruff.toml

COPY ./app /app/app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]