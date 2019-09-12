from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('morning/', views.morning, name='morning'),
    path('article/<id>/', views.view_article, name='article'),
    path('articles/<month>/<year>/', views.view_articles, name='articles'),
    path('crud/', views.crud_ops, name='crud'),
]
