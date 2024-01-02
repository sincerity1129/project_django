# Django르 활용한 인스타 페이지 만들기

### 설치 환경
    Ubuntu 22.04
    python  3.10.12

### 기본 실행 가이드
#### git code down
    git@github.com:sincerity1129/project_django.git
#### 가상 환경 설정
    cd project_django
    python -m venv venv(가상환경이름)
    source venv/bin/activate
#### 설치 라이브러리
    pip install Django==5.0 djangorestframework==3.14.0 django-storages==1.14.2

### media 파일 등록을 위한 설정
#### 폴더 설정
    프로젝트 최상단 디렉토리(project_django)
    cd project_django
    mkdir media
    cd media
    mkdir backImage  # 피드 이미지 폴더
    mkdir profile  # 프로필 이미지 폴더
#### 피드 이미지 삽입 안할 때 랜덤 이미지 들어가기 위한 설정
##### django/config/path_cfg.py(위치)
    BackGroundImageFiles # 피드 생성을 위한 랜덤 이미지 설정

### 실행 방법
    python manage.py runserver
