from django.contrib import admin
from django.urls import path, include#追記
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsapp.urls')), #追記
    path('__debug__/', include('debug_toolbar.urls')),
]