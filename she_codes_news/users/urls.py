# users/urls.py
from django.urls import path
from .views import CreateAccountView, UserProfileView
# from .views import YourAuthorStoriesDetailView

app_name ='users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    # path('author/<str:username>/', AuthorStoriesView.as_view(), name='author_stories')
]