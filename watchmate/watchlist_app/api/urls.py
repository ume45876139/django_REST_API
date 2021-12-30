from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewList,
                                    ReviewCreate,
                                    ReviewDetail, 
                                    WatchListAV, 
                                    WatchDetailAV,
                                    StreamPlatformAV, 
                                    StreamPlatformDetailAV,
                                    StreamPlatformVS,)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform'),
router.register('cast', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name= 'stream-detail'),

    path('stream/<int:pk>/review', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='stream-detailreview-create'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewList.as_view(), name='review-list')
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')

]
