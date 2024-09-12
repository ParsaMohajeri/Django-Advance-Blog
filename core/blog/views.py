from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
from django.views.generic import ListView
# Create your views here.
class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["name"]="parsa"
        context["posts"]=Post.objects.all()
        return context

class RedirectToMaktab(RedirectView):
    url="http://maktabkhooneh.org"


class PostList(ListView):
    # queryset=Post.objects.all()
    
    context_object_name="posts"
    def get_queryset(self):
        posts=Post.objects.filter(status=False)
        return posts


