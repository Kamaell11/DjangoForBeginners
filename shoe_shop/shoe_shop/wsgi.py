import os
import sys
from django.core.wsgi import get_wsgi_application

# Dodanie ścieżki nadrzędnej do sys.path, aby znaleźć settings.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ustawienie Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoe_shop.settings")

# Tworzenie aplikacji WSGI
application = get_wsgi_application()

# Wymagane przez Vercel
app = application  # Vercel wymaga zmiennej 'app'
