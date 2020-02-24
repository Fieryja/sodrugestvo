from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('stages', TemplateViewSet)

urlpatterns = [
    path('login/', csrf_exempt(login_view)),
    path('refresh_token/', csrf_exempt(user_state)),
    path('logout/', csrf_exempt(logout_view)),
]
urlpatterns += router.urls

