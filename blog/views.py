from django.shortcuts import render, redirect
from django.views import View

from .models import Blog, Comment
from .tasks import add_like_to_blog_task
from .forms import CommentForm

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            blogs = Blog.objects.select_related()[:12]
            context = {
                'blogs':blogs,
            }
        else:
            return redirect('signin')
        return render(request, 'blog/index.html', context)
        # if request.user.is_authenticated:
        #     response.set_cookie(request.user.username,f'Bu {request.user.username} nomli foydalanuvchi')
        # else:
        #     return redirect('signin')
        # return response
     
class BlogDetailView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            blog = Blog.objects.get(slug=slug)
            comments = Comment.objects.filter(blog=blog)
            blog.views += 1
            blog.save()
            #blogs = Blog.objects.filter(category__name=blog.category.first()).exclude(slug=blog.slug)[:3]
            
            form = CommentForm

            context = {
                'blog':blog,
                'comments':comments,
                'number_of_likes':blog.number_of_likes,
                'likes_number':blog.likes.count(),
                'likes':blog.likes,
                'form':form
            }
        
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
        else:
            return redirect('signin')
        return render(request, 'blog/blog-single.html', context)

    def post(self, request, slug):
        add_like_to_blog_task.delay(
            user=request.user.id, slug=slug
        )
        
        return redirect('blog:blog-detail',slug=slug)
    
class AddCommentView(View):
    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.blog = Blog.objects.get(slug=slug)
            data.user = request.user
            data.save()
            return redirect('blog:blog-detail',slug=slug)