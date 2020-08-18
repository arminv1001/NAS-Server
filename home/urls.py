from django.conf import settings
from  django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('upload', views.upload, name='upload'),
    path('download',views.download, name='download'),
    path('admin/',admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
