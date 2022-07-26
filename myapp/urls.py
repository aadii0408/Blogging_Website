
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loadhtml', views.loadhtml),
    path('', views.signup),
    path('datasave', views.datasave),
    path('login', views.login),
    path('home',views.home),
    path('aboutus',views.aboutus),
    path('company',views.company),
    path('logout',views.logout),
    path('createPost',views.createPost),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)