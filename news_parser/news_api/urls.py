from django.urls import path
from news_api import views

urlpatterns = [
    path(r'articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
]
