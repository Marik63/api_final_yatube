from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.authtoken import views

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/',
          TokenRefreshView.as_view(), name='token_refresh'),
]
