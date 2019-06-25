from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedRelatedField(
                                            read_only=True,
                                            view_name='api_post_detail',
                                            lookup_field='slug')
    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'date', 'body')
