# Django

1. 프로젝트 생성
```bash
django-admin startproject {pjt_name} .
```

2. 가상환경 생성 및 활성화
```bash
python -m venv vevn
source venv/Scripts/activate
```

3. 가상환경 내부 장고 설치
```bash
pip install django
```

4. 서버 실행 (종료: `ctrl + c`)
```bash
python manage.py runserver
```

5. app 생성
```bash
django-admin startapp {app_name}
```

6. app 등록(`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '{app_name}',
]
```
