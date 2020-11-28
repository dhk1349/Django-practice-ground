from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView


from blog.models import Post
# Create your views here.

#--- ListView
class PostLV(ListView):
    model=Post
    template_name='blog/post_all.html'
    context_object_name='posts'
    paginate_by=2
    

#---DatilView
class PostDV(DetailView):
    model=Post
    
#---ArchiveView
class PostAV(ArchiveIndexView):
    model=Post
    date_field='modify_dt'
    
class PostYAV(YearArchiveView):
    model=Post
    date_field='modify_dt'
    make_objec_list=True
    
class PostMAV(MonthArchiveView):
    model=Post
    date_field='modify_dt'
    
class PostDAV(DayArchiveView):
    model=Post
    date_field='modify_dt'
    template_name="blog/_post_archive_day.html"
    
class PostTAV(TodayArchiveView):
    model=Post
    date_field='modify_dt'
    template_name="blog/_post_archive_day.html"
    