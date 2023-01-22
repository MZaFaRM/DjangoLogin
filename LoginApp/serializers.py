from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
