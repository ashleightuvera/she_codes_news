# from django.urls import path
# from . import views
# from .views import IndexView, StoryView, AddStoryView, EditStoryView, DeleteStoryView

# app_name = 'news'

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.StoryView.as_view(), name='story'),
#     path('add-story/', views.AddStoryView.as_view(), name='newStory'),
#     path('edit_story/<int:pk>/', EditStoryView.as_view(), name='edit_story'),
#     path('delete_story/<int:pk>/', DeleteStoryView.as_view(), name='delete_story')
# ]

# urls.py
from django.urls import path
from . import views
from .views import IndexView, StoryView, AddStoryView, EditStoryView, DeleteStoryView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('edit_story/<int:pk>/', EditStoryView.as_view(), name='edit_story'),
    path('delete_story/<int:pk>/', DeleteStoryView.as_view(), name='delete_story')
]
