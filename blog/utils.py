from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Blog, Category

# def searchBlogs(request):

#     search_query = ''
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     categories = Category.objects.filter(name__icontains=search_query)

#     blogs = Blog.objects.distinct().filter(
#         Q(title__icontains=search_query)|
#         Q(body__icontains=search_query)
#     )
#     return blogs, search_query

def paginateBlogs(request, blogs, result):
    
    page = request.GET.get('page')
    paginator = Paginator(blogs, result)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blogs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        blogs = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, blogs