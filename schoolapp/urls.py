from django.conf.urls import url, include
from schoolapp import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     url(r'^users/register', views.create_user),
# ]


urlpatterns = [
    url(r'^market_channels/$', views.MarketChannelList.as_view()),
    url(r'^students/$', views.StudentList.as_view()),
]