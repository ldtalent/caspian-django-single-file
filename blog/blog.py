import os
import sys
from django import setup
from django.contrib import admin
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from decouple import config, Csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SETTINGS
settings.configure(
	DEBUG=config('DEBUG', default=False, cast=bool),
	SECRET_KEY=config('SECRET_KEY'),
	ALLOWED_HOSTS=config('ALLOWED_HOSTS', cast=Csv()),
	ROOT_URLCONF = __name__,
	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'blogapp',
	],
	MIDDLEWARE = [
		'django.middleware.security.SecurityMiddleware',
		'django.contrib.sessions.middleware.SessionMiddleware',
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.contrib.auth.middleware.AuthenticationMiddleware',
		'django.contrib.messages.middleware.MessageMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	],
	TEMPLATES = [
		{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [
				os.path.join(BASE_DIR, 'templates'),
			],
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
	],
	DATABASES={
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': ('db.sqlite3'),
		}
	},
	STATIC_URL = '/static/',
	STATICFILES_DIR = [
		os.path.join(BASE_DIR, 'static'),
	]
)

setup()


# VIEWS
def index(request):
	return HttpResponse("<h1>Hello, this is a minimal project setup. Configure as you please!</h1>")


# URLS
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='index'),
]

application = get_wsgi_application()

if __name__ == '__main__':
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)