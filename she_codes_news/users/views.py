from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import CustomUser, Story
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/create_account.html'

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user

def user_profile_view(request):
    profile = CustomUser.objects.get_or_create(user=request.user)[0]
    return render(request, 'users/profile.html', {'profile': profile})

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        author_name = self.request.GET.get('author', None)
        if author_name is not None:
            return Story.objects.filter(author__username=author_name)
        else:
            return Story.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_name = self.request.GET.get('author', None)
        if author_name is None:
            context['latest_stories'] = Story.objects.all().order_by('-created_at')[:5]
        else:
            context['filtering'] = True
        return context
