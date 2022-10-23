from rest_framework import serializers
from news.models import Article, Journalist

from datetime import datetime
from django.utils.timesince import timesince



class ArticleSerializer(serializers.ModelSerializer):
    time_since_release = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField() 
    # author = JournalistSerializer()

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


class JournalistSerializer(serializers.ModelSerializer):

    #articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail",)
    class Meta:
        model = Journalist
        fields = '__all__'
