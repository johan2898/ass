from django.contrib import admin
from .models import Stories, StoriesSeries, StoriesCategory, Dataa, telling
from tinymce.widgets import TinyMCE
from django.db import models


class StoriesAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class tellingAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(StoriesSeries)
admin.site.register(StoriesCategory)
admin.site.register(Stories, StoriesAdmin)
admin.site.register(Dataa)
admin.site.register(telling, tellingAdmin)

# Register your models here.
