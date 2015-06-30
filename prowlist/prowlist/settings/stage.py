from default import *

ALLOWED_HOSTS = []

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'prowlist',
		'USER': 'maachi',
		'PASSWORD': '89gUQ86967s3m8G',
		'HOST': 'maachi.cgcgumluvnib.us-west-2.rds.amazonaws.com',
		'PORT': '',
	}
}

AWS_S3_SECURE_URLS = False
AWS_STORAGE_BUCKET_NAME = 'prowlist'
#AWS_S3_CUSTOM_DOMAIN = 'cdn.prowlist.com'
SITE_URL = 'http://52.26.178.213'
