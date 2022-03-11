
from email.mime import base
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from clients.views import ClientViewSet
from application.views import ProjectViewSet, IssueViewSet, CommentViewSet, ContibutorViewSet

router = routers.SimpleRouter()
router.register('login', ClientViewSet, basename='login')
router.register('project', ProjectViewSet, basename='project'),
router.register('issue', IssueViewSet, basename='issue'),
router.register('comment', CommentViewSet, basename='comment')
router.register('contibutor', ContibutorViewSet, basename='contibutor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
