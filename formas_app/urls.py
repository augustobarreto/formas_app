from django.urls import include, path, re_path
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from formas_app.apps.frontend.views import FrontendView
from formas_app.apps.chatgpt.views import ChatGPTViewSet
from formas_app.apps.health.views import HealthCheckView
from formas_app.apps.oie.views import PTOIEFlairViewSet
from formas_app.apps.dptoie.views import DPTOieViewSet

router = routers.DefaultRouter()

router.register(r'chatgpt', ChatGPTViewSet, basename='chatgpt')
router.register(r'ptoieflair', PTOIEFlairViewSet, basename='ptoieflair')
router.register(r'dptoie', DPTOieViewSet, basename='dptoie')

schema_view = get_schema_view(
    openapi.Info(
        title='LABS API',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
    path ('admin/',admin.site.urls ),
    path('api/v1/', include(router.urls)),
    path('api/v1/healthcheck/', HealthCheckView.as_view(), name='healthcheck'),
    path('formasAPI/', FrontendView.as_view(), name='formasAPI')

]
