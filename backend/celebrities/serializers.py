from django.contrib.auth import get_user_model


from rest_framework import serializers

from .models import Celebrity, Photo, Rating


User = get_user_model()


class CelebritySerializer(serializers.ModelSerializer):
    # photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Celebrity
        fields = ["id", "full_name", "created_by"]

    def get_photos(self, obj):
        return Photo.objects.filter(celebrity=obj)


class CelebrityUpdateSerializer(serializers.ModelSerializer):
    # id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Celebrity
        fields = (
            "id",
            "full_name",
        )


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "id",
            "photo",
            "celebrity",
        )


class CelebrityPhotoListSearializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["photo"]


class RatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["photo", "stars", "comment"]


class PhotoRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["stars", "comment", "created_by"]
