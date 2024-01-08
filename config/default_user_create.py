from django.contrib.auth.hashers import make_password

Tester = dict(
        email = "test@naver.com",
        password = make_password('12341234'),
        realname = '테스터',
        nickname = '테스터중입니다.'
        )   