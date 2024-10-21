#!/bin/bash

alembic init alembic
alembic upgrade HEAD
exec "$@"
