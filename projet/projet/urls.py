from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from application.views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorViewset
from authentication.views import UserListViewset, SignupViewset


"""
router :
    - /projects/
    - /projects/{id}
    - /signup/
    - /userlist/
"""

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects'),
router.register(r'signup', SignupViewset, basename='signup')
router.register(r'userslist', UserListViewset, basename='userslist')

"""
Nested router :
    - /projects/{id}/users/
    - /projects/{id}/users/{id}/

    - /projects/{id}/issues/
    - /projects/{id}/issues/{id}/
"""

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'users', ContributorViewset, basename='project-users')
projects_router.register(r'issues', IssueViewSet, basename='project-issues')

"""
Nested router :
    - /projects/{id}/issues/{id}/comments/
    - /projects/{id}/issues/{id}/comments/{id}
"""

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
