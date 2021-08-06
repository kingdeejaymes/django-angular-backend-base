from django.conf.urls import url
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # Obtain Access and Refresh Token. Requires Username and Password currently in the database
    # to be passed as payload to the endpoint so this can be the login endpoint as well.
    # POST method on the API call
    # https://www.jetbrains.com/pycharm/guide/tutorials/django-aws/rest-api-jwt/
    url(r'api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint to refresh token if expired. Setting.py specify 5 mins only SIMPLE_JWT.ACCESS_TOKEN_LIFETIME
    url(r'api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint to verify if token is valid
    url(r'api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

    # App APIs
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]