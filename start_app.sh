#!/bin/bash

exec python3 /app/tinyurl/backend/write/app.py &
exec python3 /app/tinyurl/backend/read/app.py &
