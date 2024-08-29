#!/bin/sh

echo "==> Migration 파일 생성"
yes | python manage.py makemigrations --settings=kbb_roadmap.settings

echo "==> Migrate 실행"
python manage.py migrate --settings=kbb_roadmap.settings --fake-initial

echo "==> collectstatic 실행"
python manage.py collectstatic --settings=kbb_roadmap.settings --noinput -v 3

echo "==> 패키지 다운로드"
pip install -r /code/requirements.txt

echo "==> 배포!"
gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=kbb_roadmap.settings kbb_roadmap.wsgi:application