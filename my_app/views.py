from django.shortcuts import render
from django.views.generic import TemplateView, DetailView , ListView , UpdateView, DeleteView , CreateView
from .models import Post,Category
from django.urls import reverse_lazy
# Create your views here.

class IndexPageView(ListView):
	model = Post
	template_name = 'index.html'

# def indexpageview(request):
# 	posts = Post.objects.all()
# 	context = {
# 	"news":posts,
# 	}
# 	return render(request,'index.html',context)


class BasePageView(TemplateView):
	template_name = 'base.html'



class Post_DetailPageView(DetailView):
	model = Post
	template_name = 'post_detail.html'


# def detailpageview(request,news_id):
# 	post = Post.objects.filter(id=news_id)
# 	ctx = {
# 	"new":post[0]
# 	}
# 	return render(request,'post_detail.html',ctx)



#### CATEGORY PAGE

def categorypageview(request,category_id):
	category = Category.objects.get(pk=category_id)
	posts = Post.objects.all().filter(category_id=category_id)
	print(posts)
	ctx = {
	"category_name": category,
	"news": posts
	}
	return render (request,'category.html', ctx)



### update

class PostUpdateView(UpdateView):
	model = Post
	fields = ('title', 'image','body')
	template_name = 'post_edit.html'
	success_url = reverse_lazy('index')

### delete
class PostDeleteView(DeleteView):
	model = Post
	fields = ('title', 'image','body')
	template_name = 'post_delete.html'
	success_url = reverse_lazy('index')


##### create post


class PostCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ('category','title', 'body','image')
	success_url = reverse_lazy('index')



















#### UZBEKISTAN PAGEE
 
# class UzbekistanPageView(ListView):
# 	model = Post
# 	template_name = 'uzbekistan.html'


# def uzbekistanpageview(request,uzb_id):
# 	uzbekistan = Category.objects.get(pk=uzb_id)
# 	posts = Post.objects.all().filter(id=uzb_id)
# 	print(uzbekistan)
# 	ctx = {}
# 	return render (request,'category.html', ctx)


#### SPORT PAGE
# class SportPageView(ListView):
# 	model = Post
# 	template_name = 'sport.html'

# def sportpageview(request,sport_id):
# 	sport = Category.objects.get(pk=sport_id)
# 	posts = Post.objects.all().filter(id=sport_id)
# 	print(sport)
# 	ctx = {}
# 	return render (request,'sport.html', ctx)



