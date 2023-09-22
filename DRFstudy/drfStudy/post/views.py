from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer, PostUpdateSerailizer, PostRetrieveSerailizer

class PostView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            serializer.validated_data['writer'] = user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostDetailView(APIView):
    # Blog 객체 가져오기
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = PostSerializer(blog)
        return Response(serializer.data)

    # Blog 수정하기
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

# 게시물 생성
class PostCreateAPIView(generics.CreateAPIView):
    gueryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    
    def perfrom_create(self, serializer):
        serializer.save(writer = self.request.user)
        
# 사용자가 작성 한 것만 볼 수 있음
class PostUserListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(writer = user) 

# 모든 목록 다 볼 수 있음 
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 모든 목록 검색
class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()  
    serializer_class = PostRetrieveSerailizer

# 글 수정
class PostUpdateAPIView(generics.UpdateAPIView):
    gueryset = Post.objects.all()
    serializer_class = PostUpdateSerailizer
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(writer = user) 

class PostDestroyAPIView(generics.DestroyAPIView):
    gueryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    gueryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    gueryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    gueryset = Post.objects.all()
    serializer_class = PostSerializer