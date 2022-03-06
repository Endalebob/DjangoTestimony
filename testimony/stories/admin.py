from django.contrib import admin
from stories.models import *


class ModelPerson(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'ethio_phone')
    search_fields = ('first_name','phone')

    def ethio_phone(self, obj):
        return "+{} {} {} {}".format(str(obj.phone)[0:3], str(obj.phone)[3:6],
                                     str(obj.phone)[6:9], str(obj.phone)[9:13])


class ModelStory(admin.ModelAdmin):
    list_display = ('type', 'story')
    list_filter = ('person','title')
    search_fields = ('title','story','person')


class ModelComment(admin.ModelAdmin):
    list_display = ('comment_date', 'comment')
    list_filter = ('comment_date',)


_site = admin.site

_site.register(Person, ModelPerson)
_site.register(Story, ModelStory)
_site.register(Comment, ModelComment)
