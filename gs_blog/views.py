from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{'author' : 'gsk',
	 'title' : 'blog post 1',
	 'content' : 'fsre',
	 'date_posted' : '2-2-2020'
	  },
	  {'author' : 'raavan',
	 'title' : 'blog post 2',
	 'content' : 'fsfasfe',
	 'date_posted' : '2-2-2020'
	  }

]


def home(request):
	context = {
		'posts' : posts
	}
	return render(request,'gs_blog/home.html',context)

def about(request):
	return render(request,'gs_blog/about.html',{'title':'raavan'})
