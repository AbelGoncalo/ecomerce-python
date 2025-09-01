"""
URL configuration for loja project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # <- aqui está o include certo!

urlpatterns = [
    path('', include('produto.urls')),
    path('perfil/', include('perfil.urls')),   # correto
    path('pedido/', include('pedido.urls')),   # correto

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO:  Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
