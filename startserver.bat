@echo off
cd C:\japhe\latvian-arbitrage\server
call C:\japhe\latvian-arbitrage\server\.venv\Scripts\activate
python manage.py runserver
call C:\japhe\nginx\nginx
deactivate