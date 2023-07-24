from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import BlogPost, BlogAuthor, BlogComment 
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from datetime import datetime

# Create your views here.

def index(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'blog/index.html')

class BlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 5
    
class BlogDetailView(generic.DetailView):
    model = BlogPost

class AuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    model = BlogAuthor

class CreateCommentView(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        form.instance.post_date = datetime.now()
        
        return super(CreateCommentView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-detail', args=[str(self.kwargs['pk'])])
        
    def get_context_data(self, **kwargs):
        context = super(CreateCommentView, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        
        return context