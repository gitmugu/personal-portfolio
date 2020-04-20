from django.shortcuts import render, get_object_or_404
from .models import BlogData

# Create your views here.
def all_blogs(request):
	blogdatas = BlogData.objects.all()
	return render(request,'blog/all_blogs.html', {'blogdatas':blogdatas})

def blog_detail(request, blog_id):
	blog = get_object_or_404(BlogData, pk=blog_id)
	return render(request,'blog/blog_detail.html', {'blog':blog})