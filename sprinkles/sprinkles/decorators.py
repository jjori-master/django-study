import functools

from . import utils


def check_sprinkles(view_func):
    """Check if a user can add sprinkles"""

    # 내부 함수에 있는 중요한 메타데이터가 모두 외부함수로 복사됩니다.
    @functools.wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        # Act on the request object with utils.can_sprinkle()
        # noinspection PyUnresolvedReferences
        request = utils.check_sprinkle_rights(request )

        # Call the view function
        response = view_func(request, *args, **kwargs)

        # Return the HttpResponse object
        return response

    return new_view_func
