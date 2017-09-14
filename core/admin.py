from django.contrib import admin
from core.models import Urls
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl','pub_date', 'count')
    ordering = ('-pub_date',)

class UrlsResource(resources.ModelResource):

    class Meta:
        model = Urls
        verbose_name_plural = "Urls"

class UrlsAdmin(ImportExportModelAdmin):
    resource_class = UrlsResource

admin.site.register(Urls, UrlsAdmin)
