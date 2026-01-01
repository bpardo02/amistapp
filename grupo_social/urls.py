from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('noticias/', views.noticias),
    path('noticias/crear/', views.crear_noticia),

    path('recuerdos/', views.recuerdos),
    path('recuerdos/crear/', views.crear_recuerdo),

    path('resenas/', views.resenas),
    path('resenas/crear/', views.crear_resena),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
