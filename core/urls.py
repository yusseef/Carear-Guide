
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from survey import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Signin),
    path('<int:pk>', views.Survey, name='user'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)