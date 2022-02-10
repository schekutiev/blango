from rest_framework import serializers
from blog.models import Post, Tag
from blango_auth.models import User

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="value", 
        many=True, 
        queryset=Tag.objects.all(),
    )

    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), 
        view_name="api_user_detail", 
        lookup_field="email",
    )

    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]
        
# The Post API won’t work now, until we have added the api_user_detail view

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # We’re including just a subset of fields, 
        # because there’s sensitive data like the password hash 
        # which we don’t want to include.
        fields = ["first_name", "last_name", "email"]