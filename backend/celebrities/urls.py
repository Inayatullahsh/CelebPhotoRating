from django.urls import path


from .views import (
    CelebrityListCreateView,
    CelebrityDetailUpdateDestroyView,
    CelebrityPhotosList,
    RatePhotoListCreateView,
    PhotoRatingsList,
)

urlpatterns = [
    path("", CelebrityListCreateView.as_view(), name="celeb_list_create"),
    path("<int:pk>/", CelebrityDetailUpdateDestroyView.as_view(), name="celeb_detail"),
    path("<int:pk>/photos/", CelebrityPhotosList.as_view(), name="celeb_photos"),
    path("ratings/", RatePhotoListCreateView.as_view()),
    path("<int:pk>/photo/ratings/", PhotoRatingsList.as_view()),
]
