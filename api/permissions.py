from rest_framework.permissions import BasePermission


class IsHotelRelated(BasePermission):
    """
    Allows access only to hotel related users.
    """
    def has_permission(self, request, view):
        user = request.user
        print(user)
        hotel_id = view.kwargs['hotel_id']
        return (user.is_authenticated and  # logged in
                hasattr(user, 'userprofile') and  # has profile
                request.user.userprofile.hotel.id == hotel_id)  # is hotel related
