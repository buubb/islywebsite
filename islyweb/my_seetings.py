MY_SECRET = {
    "SECRET_KEY" : 'django-insecure-mo)7-bhl30!g&i7qr6@qo*03^!kfl^#*887-o=)rcog2@d&!z('
}

MY_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'login_djatjfdls',  # 각자의 로컬 데이터베이스 이름에 맞게 설정
        'USER': 'djatjfdls', #각자의 로컬 db user name ex)root, test 등등
        'PASSWORD': 'djatjfdls', #각자의 로컬 db pw ex)1234
        'HOST': 'localhost', 
        'PORT': '',  # 비워두거나 디폴트 포트(3306) 입력
    }
}