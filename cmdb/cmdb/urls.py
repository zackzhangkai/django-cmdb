from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
urlpatterns = [
    url(r'^index/$',blog_views.index,),
    url(r'^index/right.html/$',blog_views.right,),
    url(r'^index/left.html/$',blog_views.left,),
    url(r'^admin/$',admin.site.urls),
]
