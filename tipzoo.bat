@echo off
REM Activer l'environnement virtuel
call TIPZOO_ENV\Scripts\activate

REM Lancer l'application Python
python main.py

REM Désactiver l'environnement virtuel (optionnel)
deactivate