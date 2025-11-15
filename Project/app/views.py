from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm
from .models import Post
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm  # assuming you have a ModelForm
from django.views.generic import ListView

class HomePageView(ListView):
    model = Post
    template_name = 'app/home.html'  # your template that shows all posts
    context_object_name = 'posts'  # this variable is used in template

def post_list(request):
    posts = Post.objects.all()  # fetch all posts
    return render(request, 'app/home.html', {'posts': posts})



class PostCreateView(View):
    template_name = 'app/post_create.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect to home after creation
        return render(request, self.template_name, {'form': form})
    
    # def post_create(request):
    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('post_list')  # make sure this matches your URL name
    #     else:
    #         form = PostForm()
    #     return render(request, 'post_create.html', {'form': form})