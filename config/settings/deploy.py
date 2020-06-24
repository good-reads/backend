from .base import *


debug = False

# ALLOWED_HOSTS = [
#     ".ap-northeast-2.compute.amazonaws.com",
#     "54.180.154.184",
# ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# AWS settings
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id'] # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_key'] # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = config_secret['aws']['region']

# S3 Storages settings
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['storage_name'] # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'