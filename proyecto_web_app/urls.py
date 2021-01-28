'''Archivo urls.py para generar aqui las urls de la aplicacion proyecto_web_app
y luego incluirlas con la funcion include() en el archivo urls de proyecto_web
que es la carpeta principal'''

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from proyecto_web_app import views



urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)