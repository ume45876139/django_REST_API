from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
  class Meta:
    model = StreamPlatform
    fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):

  class Meta:
    model = WatchList 
    fields = "__all__"
    # fields = ['id', 'name', 'description']
    # exclude = ['active']


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