"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import webapp
import mainapp.views




urlpatterns = [
    path('', include('mainapp.urls')),
    path('main/', include('mainapp.urls')),
    path('webapp/', include('webapp.urls'), name='webapp_views'),
    path('admin/', admin.site.urls),
    # path('index', webapp.views.index, name='webapp/index'),
    path('matplotapp/', include('matplotapp.urls')),
    path('filesapp/', include('filesapp.urls')),
    path('calc/', include('calcapp.urls')),
    # path(r'^$', include('webapp.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)