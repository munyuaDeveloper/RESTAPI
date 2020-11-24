from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Blog API'  # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'  # new
schema_view = get_swagger_view(title=API_TITLE)  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger-docs/', schema_view),
]
