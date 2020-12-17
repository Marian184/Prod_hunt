
from django.contrib import admin
from django.urls import path, include
import products.views
import users.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name='home'),
    path('users/signin', users.views.signin, name='signin'),
    path('users/login', users.views.login, name='login'),
    path('users/logout', users.views.logout, name='logout'),
    path('products/', include('products.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
