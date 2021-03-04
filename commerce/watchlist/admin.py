from django.contrib import admin
from .models import watcherList
# Register your models here.


class watcherAdmin(admin.ModelAdmin):
    list_display = ("id","listID","addedBy","watchedBy")

admin.site.register(watcherList,watcherAdmin)
