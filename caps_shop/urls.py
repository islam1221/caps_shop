from django.contrib import admin
from django.urls import path, include
from main import views as cap_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/caps/', cap_view.caps_list_view),
    path('api/v1/caps/<int:id>/', cap_view.cap_detail_view),
]
