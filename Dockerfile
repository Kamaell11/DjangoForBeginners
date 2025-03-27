# Używamy lekkiego obrazu bazowego z Pythona
FROM python:3.11-slim

# Ustawienie zmiennych środowiskowych
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiowanie plików projektu do kontenera
COPY . /app/

# Instalacja zależności
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Otwarcie portu dla aplikacji
EXPOSE 8000

# Uruchomienie serwera Django
CMD ["python", "shoe_shop/manage.py", "runserver", "0.0.0.0:8000"]
