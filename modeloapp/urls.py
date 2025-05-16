from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("categorias/", include("categories.urls", namespace="categories")),
    path("produtos/", include("product.urls", namespace="products")),
    path("clientes/", include("clients.urls", namespace="clients")),
    path("pedidos/", include("order.urls", namespace="orders")),
    path('socialnetworks/', include('socialnetworks.urls', namespace="socialnetworks")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
