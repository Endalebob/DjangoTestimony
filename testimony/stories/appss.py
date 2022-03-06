from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class StoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stories'
class StoriesAdminConfig(AdminConfig):
    default_site = "admin.TestimonyAdminSite"
