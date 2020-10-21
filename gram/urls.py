from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('post/<int:post_id>/', views.post, name='post'),
    url(r'^post/(?P<image_id>\d+)', views.post, name='post'),
    path('search/', views.search_results, name='search_results')
]