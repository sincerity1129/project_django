# Django르 활용한 인스타 페이지 만들기

### 설치 환경
    Ubuntu 22.04
    python  3.10.12

### 기본 실행 가이드
#### git code
    git clone git@github.com:sincerity1129/project_django.git
#### docker install
    # package install
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg lsb-release

    # GPG key 추가
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    # repository 설정
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # docker install
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
#### docker-compose install
    # docker-compose v2 설치
    sudo rm /usr/bin/docker-compose
    mkdir -p ~/.docker/cli-plugins/
    curl -SL https://github.com/docker/compose/releases/download/v2.0.1/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
    
    # docker-compose file move
    which docker # docker가 있는 경로에 아래 심볼릭 링크 추가
    sudo ln -s ~/.docker/cli-plugins/docker-compose /usr/bin/docker-compose
    sudo ln -s ~/.docker/cli-plugins/docker-compose /usr/local/bin/

    # 권한 추가
    sudo chmod +x /usr/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
#### 가상 환경 설정
    cd project_django
    python -m venv venv(가상환경이름)
    source venv/bin/activate
#### 설치 라이브러리
    pip install Django==5.0 djangorestframework==3.14.0 django-storages==1.14.2

### 실행 방법
#### Django 실행
    python manage.py runserver
#### mysql DB 실행
    # git 최상위 폴더 이동
    docker-compose up -d