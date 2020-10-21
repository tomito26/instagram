from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:id>/',views.post,name='post'),
    path('comment/<int:id>',views.comment,name='comment'),
    path('search/',views.search_results, name='search_results')
    
]