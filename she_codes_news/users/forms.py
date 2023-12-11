<<<<<<< HEAD
# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm) :

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

# class CustomUserChangeForm(UserChangeForm) :

#     class Meta:
#         class Meta: 
#             fields = ['username', 'email']

=======
# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm) :

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm) :

    class Meta:
        class Meta: 
            fields = ['username', 'email']

>>>>>>> 03878bfb9afb741b2115699bdf46fea5f6e77e72
# about - profile