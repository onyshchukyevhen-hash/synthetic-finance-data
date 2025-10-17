@echo off
cd /d C:\Users\onysh\synthetic-finance-data

REM 1) Генерация данных и графиков
python generator.py --days 1000 --vol 0.02 --anomalies 0.05

REM 2) Обновление репо и публикация
git pull --rebase
git add demo\*.csv demo\*_price.png demo\*_volume.png
git commit -m "demo: %date% %time% синтетические ряды"
git push
