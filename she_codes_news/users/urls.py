<<<<<<< HEAD
# users/urls.py
from django.urls import path
from .views import CreateAccountView, UserProfileView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
=======
# users/urls.py
from django.urls import path
from .views import CreateAccountView

app_name ='users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), 
    name='createAccount'),
>>>>>>> 03878bfb9afb741b2115699bdf46fea5f6e77e72
]