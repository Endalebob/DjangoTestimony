from django.contrib import admin


class TestimonyAdminSite(admin.AdminSite):
    site_header = "Testimony Administration"
    site_title = "Testimony admin"
    index_title = "Testimony site admin"