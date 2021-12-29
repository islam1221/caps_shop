from django.contrib import admin
from django.urls import path, include
from main import views as cap_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/caps/', cap_view.CapListAPIView.as_view()),
    path('api/v1/caps/<int:id>/', cap_view.CapDetailAPIView.as_view()),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
