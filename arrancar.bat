@echo off
title Servidor El Racó dels Sabors
call venv\Scripts\activate
python manage.py runserver
pause