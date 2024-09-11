from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name="blog"

urlpatterns = [
    # path('fbv-index/', views.indexView, name = "fbv-index"),
    # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"Parsa"})),
    path('cbv-index/',views.IndexView.as_view(), name = "cbv-index"),
    path('go-to-index/',views.RedirectToMaktab.as_view(),name='redirect-to-maktab' )
]