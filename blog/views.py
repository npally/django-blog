from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
def index(request):
    post_list = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post':post})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('api_post_list', request=request, format=format)
    })

class ApiPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ApiPostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
