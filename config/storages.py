from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
  bucket_name = 'ink-dye'
  location = 'media'
  default_acl = 'private'
  file_overwrite = False

# class StaticStorage(S3Boto3Storage):
#   bucket_name = 'ink-dye'
#   location = 'static'
#   default_acl = 'private'