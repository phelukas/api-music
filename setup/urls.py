from django.urls import include, path, re_path
from rest_framework import routers
from core.views import artista, musica, playlist
from users.views import UserView
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Configuration about the swagger
schema_view = get_schema_view(
    openapi.Info(
        title="musicplay",
        default_version='v1',
        description="api music",
        terms_of_service="#",
        contact=openapi.Contact(email="pedro@lucas.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('musicas', musica.MusicaViewSet, basename='Musicas')
router.register('artistas', artista.ArtistaViewSet, basename='Artistas')
router.register('playlists', playlist.PlayListViewSet, basename='Playlists')
# router.register('users', user.UserSuperUserView, basename='Users')

urlpatterns = [
    # Default
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # Authenticated
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # urls about playlist
    path('playlists/<int:pk>/add/', playlist.PlayListAddView.as_view()),
    path('playlists/<int:pk>/remover/', playlist.PlayListRemoverView.as_view()),

    # urls about users
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
    # path('users/', user.UserSuperUserView.as_view())
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),

]
