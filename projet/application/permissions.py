from rest_framework.permissions import BasePermission
from .models import Contributor
from django.db.models import Q


class IsAdminAuthenticated(BasePermission):

    # LIST permissions : ex : http://127.0.0.1:8000/projects/
    def has_permission(self, request, view):
        granted_method = ('GET', 'POST')

        # Vérifier si l'utilisateur connecté est contributeur
        try:
            # L'utilisateur connecté doit être dans la base de données des contributeurs pour le projet sélectionné
            user = Contributor.objects.get(
                Q(project_id=view.kwargs['project_pk']) & Q(user=request.user)
            )

            # SuperUser a tous les accès accordés
            if request.user.is_authenticated and request.user.is_superuser:
                return True

            # AUTHOR a tous les accès accordés
            if request.user.is_authenticated and user.permissions == 'AUTHOR':
                return True

            # CONTRIBUTOR a seulement accés à GET et POST
            if (
                request.user.is_authenticated and user.permissions == 'CONTRIBUTOR' and request.method in granted_method
            ):
                return True

        except Contributor.DoesNotExist:
            print('pas de données correspondantes')

    # DETAIL permissions : ex : http://127.0.0.1:8000/projects/{id}/
    def has_object_permission(self, request, view, obj):

        # Vérifier si l'utilisateur connecté est contributeur
        try:
            # L'utilisateur connecté doit être dans la base de données des contributeurs
            user = Contributor.objects.get(
                Q(project_id=view.kwargs['project_pk']) & Q(user=request.user)
            )
            print(user)
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    True

                if user.permissions == 'AUTHOR':
                    return True

                granted_method = ('GET')

                if user.permissions == 'CONTRIBUTOR' and request.method in granted_method:
                    return True

        except Contributor.DoesNotExist:
            print('pas de données correspondantes')
