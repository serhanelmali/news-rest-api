from rest_framework import serializers




class ArticleSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    release_date = serializers.DateField()
    active = serializers.BooleanField()
    create_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(ready_only=True)