from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Post
from .forms import CreateForm
from django.urls import reverse



# Create your views here.
def home(request):
    return render(request, 'Tickets/home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    # creat / list
    
class Create(CreateView):
    models = Post
    template_name = "Tickets/create.html"
    form_class = CreateForm
    
    def get_success_url(self) -> str:
        return reverse('list')
    
    
class ListPosts(ListView):
    model = Post
    template_name = "Tickets/list.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all()
    
    
class PostDetail(DetailView):
    model = Post
    template_name = "Tickets/detail.html"
    context_object_name = 'post'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


    



