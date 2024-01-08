from django.contrib.auth.hashers import make_password

Tester = dict(
        email = "test@naver.com",
        password = make_password('12341234'),
        realname = 'test',
        nickname = 'tester'
        )   