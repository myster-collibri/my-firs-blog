
from django.contrib import admin
from django.urls import path,include
from blog.views import home,detail,search
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #a l'arriver sur la racine du serveur via 127.0.0.1:8000
    #lancement de la fonction home
    path('',home,name="home"),
    path('article/<int:id_article>',detail,name="detail"),
    path('article/recherche',search,name="search"),
    #si on appel auth on se retrouver a executer les urls de l'app app_auth
    #son home url en l'ocurence
    path('auth/',include("app_auth.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
