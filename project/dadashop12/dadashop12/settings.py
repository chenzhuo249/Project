"""
Django settings for dadashop12 project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c3y+4-%mv_5$wa8($1zxr&(%ezv0(^rrbc1ktc@)q2m#xud6#w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'user',
    'dtoken',
    'goods',
    'carts',
    'order'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dadashop12.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dadashop12.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'dadashop12',
        'NAME': 'myDada',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#STATCFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 用户上传的文件，称为 media files 【媒体文件】
# 标识出　什么样的请求是　访问　媒体文件的请求
# "http://127.0.0.1:8000/media/abc/a.jpg" --> 代表当前请求想加载媒体文件
# url 需要在主路由手动添加, static 的url是django自动添加的
MEDIA_URL = "/media/"
# 用户上传的媒体文件的储存目录，以及加载要求过来后，django去该目录下寻找资源
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if DEBUG:
    PIC_URL = "http://127.0.0.1:8000" + MEDIA_URL
else:
    pass

# CORS跨域相关
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# JWT 的 key
JWT_TOKEN_KEY = '1234567'

#from django_redis.compressors.zlib import ZlibCompressor

#   django_redis.compressors.zlib.ZlibCompressor

# redis 缓存配置
CACHES = {
    "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379", # 具体在redis中的存储位置, /1 切换库, 默认0库
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                #"PASSWORD":  123456
            }
        },

    "goods": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor" #开启压缩
            # "PASSWORD":  123456
        }
    },

    # 商品首页的缓存，独立出来，删除时暴力全删
    "goods_detail": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/6",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor"  # 开启压缩
                # "PASSWORD":  123456
            },
    },

    # 购物车数据在redis中存储，不是缓存的意思，需关闭过期时间
    "carts": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "TIMEOUT": None, #cache对象默认set为不带过期时间
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor"  # 开启压缩
            # "PASSWORD":  123456
        },


    }

}

# ??? 分布式路由前面加 / django会提醒, False 关闭
APPEND_SLASH = False

# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 固定写法
EMAIL_HOST = 'smtp.qq.com' # 腾讯QQ邮箱 SMTP 服务器地址
EMAIL_PORT = 25  # SMTP服务的端口号
EMAIL_HOST_USER = '1102225813@qq.com'  # 发送邮件的QQ邮箱
EMAIL_HOST_PASSWORD = 'evstyhswxsawjada'


#微博相关信息
WEIBO_CLIENT_ID = "2650710676" # App Key
WEIBO_CLIENT_SECRET = "ed24dc5827f16c5f243349c1ea18e44e" # App Secret
# oauth2.0 授权回调页
WEIBO_REDIRECT_URI = 'http://127.0.0.1:7000/dadashop/templates/callback.html'


