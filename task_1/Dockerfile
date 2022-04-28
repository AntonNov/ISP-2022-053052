FROM python:3.9-slim-bullseye

RUN python3 -m venv .venv

# Install dependencies:
COPY data/requirements.txt .
RUN . .venv/bin/activate && pip install -r requirements.txt

# Run the application:
COPY user_interface.py .
CMD . .venv/bin/activate && exec python user_interface.py