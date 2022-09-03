from importlib.abc import PathEntryFinder
from django.urls import path
from .views import Create, listfunc, wordlistfunc, apihomeview ,apiregi, apiroom , api_delete, apidatacreate, apiregiview

urlpatterns = [
    path('', Create.as_view(), name='home'),
    path('list/', listfunc, name='list'),
    
    path('article/<int:article_id>/', wordlistfunc, name='wordlist'),
    path('home_api',apihomeview, name='home_api'),
    path('apiregiview',apiregiview, name='apiregiview'),
    path('api_regi',apiregi, name='api_regi'),
    path('api_room/<int:api_id>/',apiroom, name='api_room'),
    path('apidatacreate/<int:api_id>/',apidatacreate, name='apidatacreate'),
    path('api_delete/<int:api_id>/', api_delete, name='api_delete'),
]
