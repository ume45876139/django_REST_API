from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)

  class Meta:
    model = WatchList 
    fields = "__all__"
    # fields = ['id', 'name', 'description']
    # exclude = ['active']

class StreamPlatformSerializer(serializers.ModelSerializer):
  # watchlist = WatchListSerializer(many=True, read_only=True)
  watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='stream-detail'
  )


  class Meta:
    model = StreamPlatform
    fields = "__all__"

  # def get_len_names(self, object):
  #   return len(object.name)

  # def validate(self, data):
  #   if dta['name'] == data['description']:
  #     raise serializers.ValidationError
  #   else:
  #     return data

  # def name_length(value):    
  #   if len(value) < 2:
  #     raise serialization.ValidationError("Name is too short!")
  #   else:
  #     return value

# def name_length(value):    
#   if len(value) < 2:
#     raise serialization.ValidationError("Name is too short!")

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[name_length])
#   description = serializers.CharField()
#   active = serializers.BooleanField() 

#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.name = validated_data('name', instance.name)
#     instance.description = validated_data('description', instance.description)
#     instance.active = validated_data('active', instance.active)
#     instance.save()
#     return instance

#   def validate(self, data):
#     if dta['name'] == data['description']:
#       raise serializers.ValidationError
#     else:
#       return data

#   # def validate(self, value):
#   #   if len(value) < 2:
#   #     raise serialization.ValidationError("Name is too short!")
#   #   else:
#   #     return value