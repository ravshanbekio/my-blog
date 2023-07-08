from django.shortcuts import render, redirect
from django.views import View

from .models import Blog, Category
from .utils import searchBlogs, paginateBlogs
from .tasks import add_like_to_blog_task

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            blogs, search_query = searchBlogs(request)
            categories_query = Category.objects.select_related()
            # paginate blogs
            custom_range, blogs = paginateBlogs(request, blogs, 12)
            
            context = {
                'categories':categories_query,
                'blogs':blogs,
                'search_query':search_query,
                'custom_range':custom_range,
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
            if request.user.is_authenticated==False:
                blog.views += 1
                blog.save()
            else:
                pass
            blogs = Blog.objects.filter(category__name=blog.category.first()).exclude(slug=blog.slug)[:3]
            
            context = {
                'blog':blog,
                'number_of_likes':blog.number_of_likes,
                'blogs':blogs,
                'likes_number':blog.likes.count(),
                'likes':blog.likes
            }
        
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
        else:
            return redirect('signin')
        return render(request, 'blog/post.html', context)

    def post(self, request, slug):
        add_like_to_blog_task.delay(
            user=request.user.id, slug=slug
        )
        
        return redirect('blog:blog-detail',slug=slug)