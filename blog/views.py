from django.shortcuts import render
from django.views import View

from .models import Blog, Category
from .utils import searchBlogs, paginateBlogs

class IndexView(View):
    def get(self, request):
        blogs, search_query = searchBlogs(request)
        categories_query = Category.objects.all()
        # paginate blogs
        custom_range, blogs = paginateBlogs(request, blogs, 12)
        context = {
            'categories':categories_query,
            'blogs':blogs,
            'search_query':search_query,
            'custom_range':custom_range,
        }
        return render(request, 'blog/index.html', context)
     
class BlogDetailView(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        if request.user.is_authenticated==False:
            blog.views += 1
            blog.save()
        else:
            pass
        blogs = Blog.objects.filter(category__name=blog.category.first()).exclude(slug=blog.slug)[:3]
        context = {
            'blog':blog,
            'blogs':blogs
        }

        return render(request, 'blog/post.html', context)
    
class AuthorView(View):
    def get(self, request):
        return render(request, 'blog/author.html')
    
# class FilterCategoriesView(View):
#     def get(self, request, category):
#         query_categories = Category.objects.filter()
#         return render(request, 'category-navbar.html')