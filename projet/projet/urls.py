
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from application.views import ProjectViewSet, IssueViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('project', ProjectViewSet, basename='project'),
router.register('issue', IssueViewSet, basename='issue'),
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
