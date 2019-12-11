import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path
from decouple import config, Csv

settings.configure(
	DEBUG=config('DEBUG', default=False, cast=bool),
	SECRET_KEY=config('SECRET_KEY', default='ba9)0r5-*o9+xs33&)gq7(7!_m7xbfas=48=%$ic003m6!(9o2'),
	ALLOWED_HOSTS=config('ALLOWED_HOSTS', cast=Csv()),
	ROOT_URLCONF = __name__,
	MIDDLEWARE_CLASSES = [
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	],
	DATABASES={
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': ('db.sqlite3'),
		}
	}
)

def index(request):
	return HttpResponse("<h1>Hello, this is a minimal project setup. Configure as you please!</h1>")

urlpatterns = [
	path('', index, name='index'),
]

application = get_wsgi_application()

if __name__ == '__main__':
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)