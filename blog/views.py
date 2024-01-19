from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # новое
from django.urls import reverse_lazy # импортируем новые методы
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import PostForm, PostImageFormSet

class BlogListView(ListView):
    model = Car
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Car
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Car
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Car
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView): # Создание нового класса
    model = Car
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
def post_detail(request, pk):
    post = get_object_or_404(Car, pk=pk)
    image_formset = PostImageFormSet(instance=post)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save()
            image_formset = PostImageFormSet(request.POST, request.FILES, instance=post)
            if image_formset.is_valid():
                image_formset.save()
                return redirect('post_detail', pk=post.pk)
    else:
        post_form = PostForm(instance=post)
