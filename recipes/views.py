from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 5
    ordering = ['-date_posted']

class UserRecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 5
    template_name = "recipes/user_recipe_list.html"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Recipe.objects.filter(author=user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.get(username=self.kwargs.get('username')).profile
        return context

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'prep_time', 'cook_time', 'instructions', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'prep_time', 'cook_time', 'instructions', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user