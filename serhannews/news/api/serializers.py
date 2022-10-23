from rest_framework import serializers
from news.models import Article

from datetime import datetime
from django.utils.timesince import timesince

class ArticleSerializer(serializers.ModelSerializer):
    time_since_release = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['id', 'release_date', 'update_date']
    
    def get_time_since_release(self, object):
        now = datetime.now()
        release_date = object.release_date
        time_delta = timesince(release_date, now)
        return time_delta

    def validate_release_date(self, value):
        today = datetime.today()
        if value > today:
            raise serializers.ValidationError("Release date can't be future!")
        return value

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.text = validated_data.get('text', instance.text)
        instance.city = validated_data.get('city', instance.city)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and description can not be same.'
            )
        return data

    def validate(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                'Title must be 20 characters length minimum.'
            )
        return value