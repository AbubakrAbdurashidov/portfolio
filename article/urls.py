from django.urls import path
from .views import blog_view, detail_view

app_name = 'article'

urlpatterns = [
    path('article/', blog_view, name='blog'),
    path('article/<slug:slug>/', detail_view, name='detail')
]