from rest_framework import serializers
from .models import user,admin_user,employee_user,scan_card,schedule_meeting

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"

class admin_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_user
        fields = "__all__"
    
class VuserSerializer(serializers.ModelSerializer):
    class Meta:
        model =employee_user
        fields ="__all__"

class scan_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model =scan_card
        fields ="__all__"

class schedule_meetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = schedule_meeting
        fields ="__all__"