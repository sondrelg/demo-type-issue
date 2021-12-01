from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.views import View


class CustomRequest(HttpRequest):
    user: User
    extra_property: int


class RequestTypeMixin:
    # This mixin would contain other functionality, but
    # the request annotation is the issue I need to get past
    # so for the mvp, that's all I'm putting here

    if TYPE_CHECKING:
        request: CustomRequest


class CostModelExperienceFeedback(RequestTypeMixin, View):
    ...
