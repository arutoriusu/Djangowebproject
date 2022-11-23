FROM python:3.9.0-alpine AS django
ENV STRIPE_API_KEY sk_test_51M6tfuBwOw8n2Hrx7I6xdheW0TD3ftWqaxP2lfu13U0b1FUiMCxzGa2fRXLaHS767lVpTnwzCywsG3LMRTEcBjt000VjzE4RwV
ENV DJANGO_STATIC_URL /admin/static/
COPY . /app
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt \
    && python3 manage.py collectstatic --noinput \
    && python3 manage.py makemigrations \
    && python3 manage.py migrate \
    && DJANGO_SUPERUSER_PASSWORD=testpass \
    && python manage.py createsuperuser --noinput --username testuser --email admin@admin.com
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]