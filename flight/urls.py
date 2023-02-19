from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from billet.views import (
    billet_list,
    billet_retrieve,
    billet_create,
    billet_update,
    billet_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('accounts/', include('allauth.urls')),
    path('', billet_list),
    path('billets/<pk>/', billet_retrieve),
    path('billets/<pk>/edit/', billet_update),
    path('billets/<pk>/delete/', billet_delete),
    path('add-billet/', billet_create),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)