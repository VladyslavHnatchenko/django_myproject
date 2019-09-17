from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('morning/', views.morning, name='morning'),
    path('article/<id>/', views.view_article, name='article'),
    path('articles/<month>/<year>/', views.view_articles, name='articles'),
    path('crud/', views.crud_ops, name='crud'),
    path('email/', views.send_mass_email, name='send_email'),
    path('static/', views.StaticView.as_view()),
    path('dreamreals/', views.DreamView.as_view()),
    path('connection/', TemplateView.as_view(template_name='login.html')),
    path('login/', views.login, name='logged_in'),
]
