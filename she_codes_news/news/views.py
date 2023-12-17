from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(generic.edit.UpdateView):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/edit_story.html'
    context_object_name = 'story'

    def get(self, request, *args, **kwargs):
        print("EditStoryView GET method executed")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("EditStoryView POST method executed")
        return super().post(request, *args, **kwargs)

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/delete_story.html'
    context_object_name = 'story'
    success_url = reverse_lazy('news:index')