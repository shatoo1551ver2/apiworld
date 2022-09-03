from django.contrib import admin
from .models import NewsUrls, News,Sentences,Words,data_NewsApi,Apis
admin.site.register(News)
admin.site.register(NewsUrls)
admin.site.register(Sentences)
admin.site.register(Words)
admin.site.register(Apis)
admin.site.register(data_NewsApi)
