# Django를 활용한 인스타 페이지 만들기
<img width="80%" src="https://private-user-images.githubusercontent.com/80209763/304993830-b11f59cf-4ed0-41b8-a11a-c126e1a57a09.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc5ODQ0NjYsIm5iZiI6MTcwNzk4NDE2NiwicGF0aCI6Ii84MDIwOTc2My8zMDQ5OTM4MzAtYjExZjU5Y2YtNGVkMC00MWI4LWExMWEtYzEyNmUxYTU3YTA5Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjE1VDA4MDI0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJmM2U1YjhjMDUzNDM3YjM4YTFjMzA1OTcwZjExYmI0ZmI4OGM1MTg2ZGU4YjZkOGM0ZTY3ZDI2OWQ3ODExMmImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.2GeSM--EKT0fvg95pyn7jca2TI_CO8_IoawxI1AZWLc"/>

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
    pip install -r requirements.txt
#### folder 추가
##### 이미지 생성 경로
    # git 최상위 폴더 이동
    mkdir media
    cd media
    # 피드 이미지 저장 경로
    mkdir backImage
    # 프로필 이미지 저장 경로
    mkdir profile
##### 기본 생성이미지 파일
    # git 최상위 경로
    vim config/path_cfg.py
    # 계정 생성 시 기본 프로필 이미지 file 경로
    DefaultProfileImagePath
    # 피드 생성 시 이미지 없으면 랜덤 생성 이미지 file 경로
    BackGroundImageFiles 

### 실행 방법
#### Django 실행
    python manage.py runserver
#### mysql DB 실행
    # git 최상위 폴더 이동
    docker-compose up -d