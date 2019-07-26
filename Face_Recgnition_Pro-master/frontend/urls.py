from django.conf.urls import url ,include
from .views import userviewset , register , PollListView , upload
#from rest_framework import routers
from rest_framework.routers import DefaultRouter, SimpleRouter
#from .api import UserViewSet

# router = DefaultRouter()
# router.register('poll', PollViewSet)

urlpatterns = [
    url(r'^api/users/', PollListView.as_view()),
    url(r'^api/users/(?P<slug>[\w-]+)/$', PollListView.as_view()),
    #url(r'aa/', views.PostList.as_view()),
    #url(r'^<int:pk>/', views.PostDetail.as_view()),
    url(r'^$', register , name='register'),
    url(r'^upload$', upload , name='upload'),
    #url(r'^user/', userview.as_view()),
]





# urlpatterns += router.urls 