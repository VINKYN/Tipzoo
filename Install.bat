@echo off
SETLOCAL

REM Définir les noms de l'environnement virtuel et du script Python
SET VENV_NAME=TIPZOO_ENV


REM Créer un environnement virtuel
echo Création de l'environnement virtuel...
python -m venv %VENV_NAME%

REM Activer l'environnement virtuel
call %VENV_NAME%\Scripts\activate

REM Installer les dépendances
echo Installation des dépendances...
pip install -r requirements.txt

REM Désactiver l'environnement virtuel
deactivate


ENDLOCAL