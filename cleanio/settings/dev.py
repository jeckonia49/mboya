from cleanio.settings.base import *


LOCAL_APPS = [
    "accounts",
    "order",
    ]

FRAMEWORK_APPS = [
    'cloudinary_storage',
    'cloudinary',
]

INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += FRAMEWORK_APPS


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY"),
    'API_SECRET': os.environ.get("CLOUDINARY_SECRET_KEY")
}

# STATIC MEDIA FILES
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
MEDIA_URL = '/media/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# CONTEXT_PROCESSORS
CONTEXT_PROCESSORS = [
    "cleanio.context_processors.cleanio_site_context",
]
TEMPLATES[0]['OPTIONS']['context_processors'] += CONTEXT_PROCESSORS

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY #password associated with above email-id
EMAIL_PORT = 587
EMAIL_USE_TLS = True



SITE_CONTACT_TELEPHONE="0769328563"


# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': 'cleanio-mboya',
# 		'USER': 'cleanio',
# 		'PASSWORD': 'Mzeemara@123',
# 		'HOST':'cleanio.mysql.pythonanywhere-services.com',
# 		'PORT':'3306',
# 	}
# }