from django.contrib import admin
from core.models import Urls
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UrlsResource(resources.ModelResource):
    class Meta:
        model = Urls

class UrlsAdmin(ImportExportModelAdmin):
    resource_class = UrlsResource
    list_display = ('short_id','httpurl','pub_date', 'count')
    search_fields = ('short_id', 'httpurl', 'pub_date')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)
