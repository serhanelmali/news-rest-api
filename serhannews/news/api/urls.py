from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('authors/', api_views.JournalistListCreateApiView.as_view(), name='journalist-list'),
    path('articles/', api_views.ArticleListCreateApiView.as_view(), name='article-list'),
    path('articles/<int:pk>', api_views.ArticleDetailApiView.as_view(), name="article-detail"),
]