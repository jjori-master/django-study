from django.core.exceptions import PermissionDenied
from django.http import HttpRequest


def check_sprinkle_rights(request: HttpRequest) -> HttpRequest:
    if request.user.is_staff:
        return request

    # noinspection PyUnresolvedReferences
    if getattr(request.user, 'can_sprinkle', None) and not request.user.can_sprinkle:
        return request

    # Return a HTTP 403 back to the user
    raise PermissionDenied
