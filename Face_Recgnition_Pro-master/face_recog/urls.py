"""face_recognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url ,include
from django.conf import settings
from frontend.views import register , LoginView , LogoutView
from django.conf.urls.static import static

# app_name = 'users'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^' , include('frontend.urls')),
    url(r'^api/auth/login/', LoginView.as_view()),
    url(r'^api/auth/logout/', LogoutView.as_view()),
    
    # path('api/v1/auth/login/', LoginView.as_view()),
    # path('api/v1/auth/logout/', LogoutView.as_view()),
    #url(r'^rest-auth/', include('rest_auth.urls'))
    #path('admin/', admin.site.urls),
    #url(r'^$', include('frontend.urls')),
    #url(r'^$', register , name='register'),
    #url(r'^users/', include('frontend.urls')),
    #path('', include('frontend.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
