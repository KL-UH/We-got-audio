from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from convert import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('file/',views.file,name="file"),
    path('convertor',views.convertor),
    path('file/files',views.files,name="files")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
