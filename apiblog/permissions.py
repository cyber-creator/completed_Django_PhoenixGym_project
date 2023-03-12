from rest_framework import permissions
# our permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsCoachOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.groups.exists():
            group_list = []
            for groups in request.user.groups.all():
                group_list.append(str(groups).lower())

            if 'coaches' in group_list:
                return True

        return False


