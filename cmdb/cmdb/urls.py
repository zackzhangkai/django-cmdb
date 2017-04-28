from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
urlpatterns = [
    url(r'^$',blog_views.index,),
    url(r'^upload/$',blog_views.upload,),
    url(r'^postok/$',blog_views.postok,),
    url(r'^right.html/$',blog_views.right,),
    url(r'^left.html/$',blog_views.left,),
    url(r'^admin/',admin.site.urls),
]
