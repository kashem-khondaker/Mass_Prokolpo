from rest_framework.permissions import BasePermission , SAFE_METHODS , AllowAny , IsAuthenticated

# A. Role-Based Permissions (RBAC)

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'STUDENT'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MANAGER'

class IsMonitor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MONITOR'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'


# B. Action-Based Permissions (CRUD Operations)

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsBookingActionAllowed(BasePermission):
    """
    Custom permission to manage room booking access:
    - STUDENT: Can create and view own booking.
    - MONITOR: Can create, view, update, delete any booking.
    - ADMIN: Full access.
    """

    def has_permission(self, request, view):
        # Create / View access
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return request.user.is_authenticated
        if request.method == 'POST':
            return request.user.role in ['STUDENT', 'MONITOR', 'ADMIN']
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.role in ['MONITOR', 'ADMIN']
        return False

    def has_object_permission(self, request, view, obj):
        # STUDENT can only view their own
        if request.user.role == 'STUDENT':
            return request.method in SAFE_METHODS and obj.user == request.user

        # MONITOR and ADMIN can view/edit/delete everything
        if request.user.role in ['MONITOR', 'ADMIN']:
            return True

        return False



