from rest_framework import serializers
from .models import Tags, Socials, Country, Portfolio


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    socials = SocialsSerializer(many=True)
    tags = TagsSerializer(many=True)
    country = CountrySerializer()

    class Meta:
        model = Portfolio
        fields = ['name','link','socials','tags','country']
