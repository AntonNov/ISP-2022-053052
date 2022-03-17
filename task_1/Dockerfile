FROM python:3.9-slim-bullseye

RUN python3 -m venv .venv

# Install dependencies:
COPY requirements.txt .
RUN . .venv/bin/activate && pip install -r requirements.txt

# Run the application:
COPY main.py .
CMD . .venv/bin/activate && exec python main.py