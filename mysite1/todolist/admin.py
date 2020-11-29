from django.contrib import admin

from .models import Diary, Comment

class DiaryAdmin(admin.ModelAdmin):
    search_fields=['subject']

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Comment)
