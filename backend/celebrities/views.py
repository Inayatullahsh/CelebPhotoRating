from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from icecream import ic

from .models import Celebrity, Photo, Rating
from .serializers import (
    CelebritySerializer,
    CelebrityUpdateSerializer,
    CelebrityPhotoListSearializer,
    PhotoRatingsSerializer,
    PhotoSerializer,
    RatePhotoSerializer,
)
from .permissions import (
    IsPhotoOwnerOrReadOnly,
    IsOwnerOrReadOnly,
)


class CelebrityListCreateView(ListCreateAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer
    permission_classes = [IsOwnerOrReadOnly]


class CelebrityDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebrityUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CelebrityPhotosList(ListAPIView):
    serializer_class = CelebrityPhotoListSearializer

    def get_queryset(self):
        try:
            celebrity = Celebrity.objects.get(pk=self.kwargs["pk"])
        except Celebrity.DoesNotExist:
            raise Http404

        return Photo.objects.filter(celebrity=celebrity)


class RatePhotoListCreateView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatePhotoSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class PhotoRatingsList(ListAPIView):
    serializer_class = PhotoRatingsSerializer

    def get_queryset(self):

        try:
            photo = Photo.objects.get(pk=self.kwargs["pk"])
        except Celebrity.DoesNotExist:
            raise Http404

        return Rating.objects.filter(photo=photo)
