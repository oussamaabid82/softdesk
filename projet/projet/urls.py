from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from application.views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorViewset
from authentication.views import UserListViewset, SignupViewset

router = routers.SimpleRouter()
router.register(r'signup', SignupViewset, basename='signup')
router.register(r'users', UserListViewset, basename='users')
router.register(r'projects', ProjectViewSet, basename='projects'),

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'users', ContributorViewset, basename='project-users')
projects_router.register(r'issues', IssueViewSet, basename='project_issues')

issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
]
