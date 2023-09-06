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
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL #sender's email-id
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") #password associated with above email-id


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