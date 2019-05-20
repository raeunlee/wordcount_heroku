from django.contrib import admin
from django.urls import path,include
import blog.views
import wordapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    path('blog/<int:blog_id>',blog.views.detail, name="detail"),
    path('blog/new/',blog.views.new, name="new"),
    path('blog/create',blog.views.create, name="create"),

    path('wordapp/',include('wordapp.urls')),
]
