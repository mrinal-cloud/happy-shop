from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header="HappyShop"
admin.site.index_title="Welcome to happy shop Admin Panel"
admin.site.site_title="Happy-shop Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shop.urls")),
    path('blog/', include("blog.urls")),
    path('shop/', include("shop.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
