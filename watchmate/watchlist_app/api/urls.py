from django.urls import path, include
# from .views import movie_list, movie_details
# from .views import MovieLListAV, MovieDetailAV

from .views import WatchListAV, WatchListDetailAV, StreamPlatformDetailAV, StreamPlatformAV,\
    ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS, UserReviewList, WatchListGV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
# urlpatterns = [
#     path('list', movie_list, name='movie_list'),
#     path('<int:pk>', movie_details, name='movie_details')
# ]

# urlpatterns = [
#     path('list', MovieLListAV.as_view(), name='movie_list'),
#     path('<int:pk>', MovieDetailAV.as_view(), name='movie_details')
# ]

urlpatterns = [
    path('list', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watch_details'),

    path('list2/', WatchListGV.as_view(), name='watch_list2'),

    # path('stream', StreamPlatformAV.as_view(), name="streamplatform"),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),

    path('', include(router.urls)),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail")

    path('<int:pk>/create-review/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),

    path('reviews/<str:username>', UserReviewList.as_view(), name="user-reviews"),
    path('reviews/', UserReviewList.as_view(), name="user-reviews")
]