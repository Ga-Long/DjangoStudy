from rest_framework import serializers
from .models import Post, Comment

# comment all field serializer        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # 'comments' 필드 추가

    class Meta:
        model = Post
        fields = '__all__'
        
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','image', 'content']
        
        
class PostUpdateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['view_count', 'likes', 'writer']
        
        
class PostRetrieveSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


        
