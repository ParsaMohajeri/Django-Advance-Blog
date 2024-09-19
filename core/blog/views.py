from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
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


class PostListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    queryset=Post.objects.filter(status=True)
    # model=Post
    paginate_by=4
    ordering='-published_date'
    context_object_name="posts"
    # def get_queryset(self):
    #     posts=Post.objects.filter(status=True)
        # return posts


class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post


"""
class PostCreateView(FormView):
    template_name='contact.html'
    form_class=PostForm
    success_url='/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

"""
class PostCreateView(LoginRequiredMixin,CreateView):
    permission_required='blog.view_post'
    model=Post
    # fields=['author', 'title', 'content','status','category','published_date']
    form_class=PostForm
    success_url='/blog/post/'


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)





class PostEditView(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=PostForm
    success_url='/blog/post/'




class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url="/blog/post/"


