from django.contrib import admin
from django.urls import path

from uploader.views import checkUsers, registerUsers, uploadFiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', checkUsers),
    path('users/register/', registerUsers),
    path('uploadfile/', uploadFiles)
]