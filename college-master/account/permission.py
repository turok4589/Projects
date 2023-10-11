from rest_framework.permissions import BasePermission

class IsGymMember(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has a gym membership
        return request.user and request.user.gym_membership
