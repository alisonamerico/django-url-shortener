from django.db import models
from django.contrib.auth.models import User


class Urls(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    user = models.ForeignKey(User, null=True)
    search_fields = ('short_id', 'httpurl', 'pub_date')

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'

def __str__(self):
    return self.httpurl
