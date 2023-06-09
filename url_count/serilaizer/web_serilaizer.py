from rest_framework import serializers


class Webcount(serializers.Serializer):
    url = serializers.CharField(required=True)
    like = serializers.BooleanField(required=False)