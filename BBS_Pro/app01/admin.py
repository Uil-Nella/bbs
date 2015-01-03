from django.contrib import admin
from app01 import models
# Register your models here.
class BBS_admin(admin.ModelAdmin):
    list_display=('title','summary','author','signature','view_count','created_at')
    list_filter = ('created_at',)
    search_fields=('title','author__user__username')
    
    def signature(self,object):
        return object.author.signature
    signature.short_description='hei'
admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)