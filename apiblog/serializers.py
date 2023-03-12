from django.contrib.auth import get_user_model
from rest_framework import serializers
from gym.models import Blog, BlogCategory


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'date_added', 'slug', 'category', 'blog_text', 'special_text', 'blog_text_next',
                  'poster', 'youtube_link',)


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
