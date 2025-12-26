@echo off
REM Activa el entorno virtual llamado "env"
call env\Scripts\activate.bat

REM Mensaje opcional
echo Entorno virtual 'env' activado.

REM Mantener la consola abierta
python manage.py runserver
cmd
