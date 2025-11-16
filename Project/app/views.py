from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm
from .models import Post
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm  # assuming you have a ModelForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

class HomePageView(ListView): 
    #LIST VIEW=======================
    model = Post
    template_name = 'app/home.html'  # your template that shows all posts
    context_object_name = 'posts'  # this variable is used in template

def post_list(request):
    posts = Post.objects.all()  # fetch all posts
    return render(request, 'app/home.html', {'posts': posts})



class PostCreateView(View):
    #CREATE VIEW======================
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
    


class PostDetailView(DetailView):
     model = Post
     template_name = 'app/post_detail.html'  # specify your template
     context_object_name = 'post'

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a print or log statement to ensure it's rendering the view correctly
        print(f"Rendering Post Detail for: {context['post'].title}")  # Debugging line
        return context
    
    # def post_create(request):
    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('post_list')  # make sure this matches your URL name
    #     else:
    #         form = PostForm()
    #     return render(request, 'post_create.html', {'form': form})