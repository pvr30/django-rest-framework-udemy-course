from rest_framework import serializers
# from watchlist_app.models import Movie
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist =  serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watch_details'
    # )
    class Meta:
        model = StreamPlatform
        fields = "__all__"



"""Model Serializer"""
# class MovieSerializer(serializers.ModelSerializer):
#     name_length = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ['name', 'description']
#         # exclude = ['active']
#
#     # SerializerMethodField
#     def get_name_length(self, object):
#         return len(object.name)
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     """ Validation """
#     # Field Level Validation
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Name is too short!')
#         return value
#
#     # Object Level Validation
#     def validate(self, data):
#         try:
#             movie = Movie.objects.get(name=data['name'])
#         except:
#             movie = None
#
#         if movie:
#             raise serializers.ValidationError("Movie is already exists")
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should not be same!')
#         return data

#
# def description_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('Description is too short!')
#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length]) # validators
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     """ Validation """
#     # Field Level Validation
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Name is too short!')
#         return value
#
#     # Object Level Validation
#     def validate(self, data):
#         try:
#             movie = Movie.objects.get(name=data['name'])
#         except:
#             movie = None
#
#         if movie:
#             raise serializers.ValidationError("Movie is already exists")
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should not be same!')
#         return data
