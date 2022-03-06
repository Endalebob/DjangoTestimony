from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('stories/', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.comments, name='book_detail'),
    path('story-search/', views.story_search, name='book_search')
]