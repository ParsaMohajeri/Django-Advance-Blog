from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
# Create your views here.


# function base view shows a Template
"""
def indexView(request):

    name="parsa"
    context={"name":name}
    return render(request, "index.html",context)
"""
class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["name"]="parsa"
        context["posts"]=Post.objects.all()
        return context


"""FBV for redirect
from django.shortcuts import redirect
def RedirectToMaktab(request):
    return redirect('https://maktabkhooneh.org/')
"""
class RedirectToMaktab(RedirectView):
    url="http://maktabkhooneh.org"
    