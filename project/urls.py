from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("", include("api.urls")),
    path("maps/", include("maps.urls")),
    path("homepage/", views.homepage, name="homepage"),
    path(
        "notification/<int:recipient_pk>/",
        views.send_notification,
        name="send_notification",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
