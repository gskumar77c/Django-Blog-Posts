from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import Myform




def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request,'gs_blog/home.html',context)

def about(request):
	return render(request,'gs_blog/about.html',{'title':'raavan'})


def lgin(request):
	ctx = {}
	ctx['form'] = Myform()
	return render(request,'gs_blog/lgin.html',ctx)