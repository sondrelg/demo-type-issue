from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.views import View


class CustomRequest(HttpRequest):
    user: User
    extra_property: int


class RequestTypeMixin:
    if TYPE_CHECKING:
        request: CustomRequest
    ...


class OptionA(View, RequestTypeMixin):
    if TYPE_CHECKING:
        request: CustomRequest


class TypedView(View):
    if TYPE_CHECKING:
        request: CustomRequest


class OptionB(TypedView):
    pass
