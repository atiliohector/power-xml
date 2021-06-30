from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xml/', include('app.xml_generator.urls'))
]
