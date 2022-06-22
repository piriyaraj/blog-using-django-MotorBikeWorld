from django.views import generic
from .models import Bikepost, Biketable
from django.shortcuts import render

class PostList(generic.ListView):
    queryset = Bikepost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Bikepost
    template_name = 'post_detail.html'

def home(request):
    queryset = Bikepost.objects.filter(status=1).order_by('-created_on')
    return render(request,'index.html',{"bikepost_list":queryset})

def post(request,slug):
    context = {}

    # add the dictionary during initialization
    context["bikepost"] = Bikepost.objects.get(slug=slug)
    # context['biketable']=Biketable.objects.get(id=context['bikepost'].table.id)
    # print(context['biketable'].name)
    return render(request, "post_detail.html", context)
