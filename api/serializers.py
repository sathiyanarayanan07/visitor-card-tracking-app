from rest_framework import serializers
from .models import user,admin_user

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"

class admin_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_user
        fields = "__all__"