from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.get_fields()]

class FaceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Face._meta.get_fields()]

class FaceCommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FaceComment._meta.get_fields()]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Face, FaceAdmin)
admin.site.register(FaceComment, FaceCommentAdmin)
